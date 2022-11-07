from pymap.rpc.request import RpcRequest
from pymap.rpc.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)
from pymap.tools.utils import askYesNo
import math
import logging


class MakaluApiMethods(RpcRequest):
    def __init__(self, **kw) -> None:
        super(MakaluApiMethods, self).__init__(**kw)

    def _get_validator_data(self) -> list:
        """
        Get the current validator data.

        Returns
        -------
        Json Response

        Raises
        ------
        InvalidRPCReplyError
            If received unknown result from endpoint

        API Reference
        -------------

        """

        method = "queryValidatorData"
        params = None
        try:
            return self.rpc_request(
                method,
                params=params,
                endpoint=self._makalu_api_url,
                timeout=self._timeout,
                call_type="GET",
            )["data"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, self._makalu_api_url) from e

    def query_validator_data(self) -> tuple:
        data = self._get_validator_data()
        return data

    def _get_rewards_list(self, address, page=1, size=10) -> list:
        """
        Get the current rewards for a validator.

        Returns
        -------
        Json Response

        Raises
        ------
        InvalidRPCReplyError
            If received unknown result from endpoint

        API Reference
        -------------

        """

        method = "queryRewardList"
        params = dict(address=address, page=page, size=size)
        try:
            return self.rpc_request(
                method,
                params=params,
                endpoint=self._makalu_api_url,
                timeout=self._timeout,
                call_type="GET",
            )["data"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, self._makalu_api_url) from e

    def get_rewards_list(
        self,
        address: str = "",
        page: int = 1,
        size: int = 2,
        paginate: str = "Yes",
        auto_paginate: bool = True,
        show: bool = True,
    ) -> int:
        if not address:
            vals = self.handle_input(
                {"default_address": self.default_address, "paginate": paginate}
            )
            address = vals.get("default_address")
            paginate = vals.get("paginate")

        rewards_list = self._get_rewards_list(address, page=page, size=size)
        self.total_list += rewards_list.get("list")
        pages_msg, m = self.calc_num_pages(page, size, rewards_list)

        if show and not auto_paginate:
            meta = {
                "voterReward": ("", " $MAP", False, {}),
                "reward": ("", " $MAP", False, {}),
            }

            ignore = "rewardStr", "voterRewardStr"

            self.display_dict(rewards_list["list"], meta=meta, ignore=ignore)
            print(f"Rewards for [ {address} ]\n{pages_msg}")

        self.run_pagniate(
            self.get_rewards_list,
            m,
            *(address,),
            page=page,
            size=size,
            paginate=paginate,
            auto_paginate=auto_paginate,
        )
        return rewards_list

    total_list = []

    def get_epochs_in_range(self, epochs_range: str) -> list:
        epochs_in_range = None

        if epochs_range.lower().strip() != "all":
            epochs = epochs_range.split("-")
            if len(epochs) == 2:
                _from, _to = epochs
            else:
                _from = _to = epochs_range
            try:
                epochs_in_range = [x for x in range(int(_from), int(_to) + 1)]
                return True, epochs_in_range
            except ValueError as e:
                logging.error(
                    f"Incorrect epoch passed.  Got {epochs_range} expected a single epoch 32 or a range 1-10 or all "
                )
                return False, []
        return True, []

    def aggregate_rewards_list(self, epochs_in_range: list = []) -> float:
        total_rewards = 0
        total_voter_rewards = 0

        for x in self.total_list:
            e = int(x.get("epoch"))
            r = float(x.get("reward"))
            v = float(x.get("voterReward"))
            if not epochs_in_range:
                total_rewards += r
                total_voter_rewards += v
            else:
                if e in epochs_in_range:
                    total_rewards += r
                    total_voter_rewards += v

        return round(total_rewards, 2), round(total_voter_rewards, 2)

    def get_total_rewards(self, address: str = "", epochs_range: str = "all") -> dict:
        self.total_list = []
        if not address:
            vals = self.handle_input(
                {"default_address": self.default_address, "epochs_range": epochs_range}
            )
            address = vals.get("default_address")
            epochs_range = vals.get("epochs_range")

        found, epochs_in_range = self.get_epochs_in_range(epochs_range)

        if not found:
            return 0, 0

        self.get_rewards_list(
            address, show=False, page=1, size=100, paginate="Yes", auto_paginate=True
        )

        total_rewards, total_voter_rewards = self.aggregate_rewards_list(
            epochs_in_range
        )

        result = {
            "Epoch Range": epochs_range,
            "Rewards": total_rewards,
            "Voter Rewards": total_voter_rewards,
        }

        msg = "Total Rewards summary:\n\n"
        msg += "".join([f"{k:>13}: {v}\n" for k, v in result.items()])

        self.star_surround(msg)

        return result

    def _get_commitee_info_by_address(self, address) -> list:
        """
        Get the current status information for a validator.

        Returns
        -------
        Json Response

        Raises
        ------
        InvalidRPCReplyError
            If received unknown result from endpoint

        API Reference
        -------------

        """

        method = "queryCommitteeInfoByAddress"
        params = dict(address=address)
        try:
            return self.rpc_request(
                method,
                params=params,
                endpoint=self._makalu_api_url,
                timeout=self._timeout,
                call_type="GET",
            )["data"]
        except KeyError as e:
            raise InvalidRPCReplyError(method, self._makalu_api_url) from e

    def get_commitee_info_by_address(
        self, address: str = "", show: bool = True
    ) -> dict:
        msg = None
        msg_dict = {}
        if not address:
            vals = self.handle_input({"default_address": self.default_address})
            address = vals.get("default_address")

        validator_info = self._get_commitee_info_by_address(address)

        if validator_info:
            validator_info = validator_info.get("committeeBasicInfo")
            apy = self.get_apy(address)
            validator_info = {**{"apy": apy}, **validator_info}
            meta = {
                "voteReward": (None, "%", True, {}),
                "apy": (None, "%", False, {}),
                "lockedAmount": (None, None, True, dict(show_decimals=False)),
                "votePercent": (None, "%", False, {}),
                "version": (" Epoch", None, False, {}),
                "upTime": (None, "%", False, {}),
                "blockNumber": (None, "", True, dict(d=0, show_decimals=False)),
                "votedAmount": (None, "", True, dict(show_decimals=False)),
                "activeAmount": (None, "", True, dict(show_decimals=False)),
            }

            ignore = "pk1, pk2"

            res, msg, msg_dict = self.display_dict(
                [validator_info], meta=meta, ignore=ignore, show=show
            )
            if show:
                if not res:
                    print(f"Error with displaying:  {validator_info}")
                print(f"Information for Validator [ {address} ]\n")
        return validator_info, msg, msg_dict

    def calc_num_pages(self, page: int, size: int, d: dict) -> tuple:
        total = d.get("total")
        m = math.ceil(total / size)
        return (
            f"Results Per Page: {size}\nPage {page if total else 0} of {m}\nTotal Records:  {total}\n",
            m,
        )

    def run_pagniate(
        self,
        func,
        m,
        *args,
        page: int = 1,
        size: int = 2,
        paginate: str = "Yes",
        auto_paginate: bool = False,
        **kw,
    ) -> None:
        next_page = page + 1
        if not paginate:
            paginate = "No"
        do_paginate = askYesNo("", paginate)
        if do_paginate and next_page <= m:
            if not auto_paginate:
                input(f"Press any key to load page {next_page}")
            return func(
                *args,
                page=next_page,
                size=size,
                paginate=paginate,
                auto_paginate=auto_paginate,
                **kw,
            )

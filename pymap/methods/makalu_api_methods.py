from re import M
from pymap.rpc.request import RpcRequest
from pymap.rpc.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)
from pymap.tools.utils import readable_price
import math


class MakaluApiMethods(RpcRequest):
    def __init__(self, **kw) -> None:
        super(MakaluApiMethods, self).__init__(**kw)

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
        paginate: bool = True,
        show: bool = True,
    ) -> int:
        if not address:
            vals = self.handle_input(
                {"default_address": self.default_address, "pagniate": paginate}
            )
            address = vals.get("default_address")
            paginate = vals.get("paginate")

        rewards_list = self._get_rewards_list(address, page=page, size=size)
        pages_msg, m = self.calc_num_pages(page, size, rewards_list)

        if show:
            meta = {"voterReward": ("Block: ", "", True)}

            ignore = "rewardStr, voterRewardStr"

            self.display_dict(rewards_list["list"], meta=meta, ignore=ignore)
            print(f"Rewards for [ {address} ]\n{pages_msg}")

        self.run_pagniate(
            self.get_rewards_list,
            m,
            *(address,),
            page=page,
            size=size,
            paginate=paginate,
        )
        return rewards_list

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
        if not address:
            vals = self.handle_input({"default_address": self.default_address})
            address = vals.get("default_address")

        validator_info = self._get_commitee_info_by_address(address)

        if validator_info:
            validator_info = validator_info.get("committeeBasicInfo")
            if show:
                meta = {
                    "voteReward": (None, "%", True),
                    "lockedAmount": (None, None, True),
                    "votePercent": (None, "%", False),
                    "version": (" Epoch", None, False),
                    "upTime": (None, "%", False),
                    "blockNumber": (None, "", True),
                    "votedAmount": (None, "", True),
                }

                ignore = "pk1, pk2"

                res, msg = self.display_dict([validator_info], meta=meta, ignore=ignore)
                if not res:
                    print(f"Error with displaying:  {validator_info}")
                print(f"Information for Validator [ {address} ]\n")
        return validator_info, msg

    def calc_num_pages(self, page: int, size: int, d: dict) -> tuple:
        total = d.get("total")
        m = math.ceil(total / size)
        return (
            f"Results Per Page: {size}\nPage {page if total else 0} of {m}\nTotal Records:  {total}\n",
            m,
        )

    def run_pagniate(
        self, func, m, *args, page: int = 1, size: int = 2, paginate: bool = True, **kw
    ) -> None:
        next_page = page + 1
        if paginate and next_page <= m:
            input(f"Press any key to load page {next_page}")
            return func(*args, page=next_page, size=size, paginate=paginate, **kw)

import logging as log
from time import sleep
import datetime
from pymap.base.base_mixin import BaseMixin

from pymap.includes.config import alert_envs

from pymap.tools.general import General
from pymap.monitor.alerts.send_alerts import Alerts
from pymap.monitor.includes.monitor_setup import times_sent


class Monitor(BaseMixin, General, Alerts):

    start_time = datetime.datetime.now()
    current_block = 0
    first_run = True
    alert_sent = False
    times_sent = times_sent

    def __init__(self, **base_fields: dict) -> None:
        self.RUN_EVERY_X_SECONDS = self.calc_seconds()
        self.automatic = True
        super(Monitor, self).__init__(**base_fields)

    def calc_seconds(self):
        try:
            hh, mm = alert_envs.HOURS, alert_envs.MINS
            return int(float(hh) * 3600 + float(mm) * 60)
        except ZeroDivisionError:
            return 0

    def is_time_to_check(self) -> bool:
        # is it time to check?
        self.time_check = datetime.datetime.now()
        self.time_calc = (self.time_check - self.start_time).seconds

        if self.time_calc >= (self.RUN_EVERY_X_SECONDS) or self.first_run:
            self.start_time = self.time_check
            return True
        return False

    def check_sync(self, rpc, local) -> bool:
        synced = int(rpc) - int(local)
        if synced <= int(alert_envs.ACCEPTABLE_RANGE):
            return True, synced
        return False, synced

    def check_uptime(self) -> tuple:
        address = alert_envs.VALIDATOR_ADDRESS
        raw, info_str, info_dict = self.get_commitee_info_by_address(
            address, show=False
        )
        uptime = raw.get("upTime")
        if uptime:
            uptime = round(float(uptime), 2)
            if uptime < float(alert_envs.ACCEPTABLE_UPTIME):
                return False, info_str, info_dict, uptime
        return True, info_str, info_dict, uptime

    def check_peers(self) -> tuple:
        self.admin_peers_length()
        peers = self.num_peers
        data = self.query_validator_data()
        total_validators = data.get("count")

        return total_validators == peers, total_validators, peers

    def start_monitor(self) -> None:
        while 1:
            try:
                if self.is_time_to_check():
                    epoch = self.get_epoch_data()
                    _, rpc_block, local_block, _ = self.compare_block_numbers()
                    sync_res, synced = self.check_sync(rpc_block, local_block)
                    uptime_res, _, info_dict, uptime = self.check_uptime()
                    peers_res, total_validators, num_peers = self.check_peers()

                    msg_dict = {
                        "Node Statistics": " ",
                        "Epoch": epoch,
                        "Difference": (synced, sync_res),
                        "Local Block": local_block,
                        "RPC Block": rpc_block,
                        "Connected Peers": (f"{num_peers} / {total_validators}", peers_res),
                        "Uptime": (f"{uptime}%", uptime_res),
                    }
                    ignore = (
                        "version",
                        "createdAt",
                        "signAddress",
                        "accountAddress",
                        "id",
                        "blockNumber",
                    )
                    msg_dict.update(
                        {k: v for k, v in info_dict.items() if k not in ignore}
                    )
                    alert_msg = self.build_html_message("", msg_dict)
                    problem = (
                        True if False in (sync_res, uptime_res, peers_res) else False
                    )

                    if problem:
                        self.send_error_message(alert_msg, epoch)
                    else:
                        self.times_sent = self.happy_alert(
                            self.times_sent,
                            epoch,
                            alert_msg,
                            first_run=self.first_run,
                        )

                    self.first_run = False

            except Exception as e:
                log.error(e)
                self.generic_error(e)
                # error sleep....zzzzzzzzz
                if alert_envs.DELAY_IN_MINS != int(0):
                    sleep(alert_envs.DELAY_IN_MINS * 60)

            # Hot reload Env
            alert_envs.load_envs()

import logging as log
from time import sleep
import datetime

from pymap.includes.config import alert_envs
from pymap.methods.marker_methods import MarkerMethods
from pymap.methods.makalu_api_methods import MakaluApiMethods
from pymap.tools.general import General
from pymap.monitor.alerts.send_alerts import Alerts
from pymap.monitor.includes.monitor_setup import times_sent


class Monitor(MarkerMethods, MakaluApiMethods, General, Alerts):

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
        info_dict, info_str = self.get_commitee_info_by_address(address, show=False)
        uptime = info_dict.get("upTime")
        if uptime:
            uptime = round(float(uptime), 2)
            if uptime < float(alert_envs.ACCEPTABLE_UPTIME):
                return False, info_str, uptime
        return True, info_str, uptime

    def start_monitor(self) -> None:
        while 1:
            problem = False
            try:
                if self.is_time_to_check():
                    epoch = self.get_epoch_data()
                    _, rpc_block, local_block, msg = self.compare_block_numbers()
                    sync_res, synced = self.check_sync(rpc_block, local_block)
                    if not sync_res:
                        problem = True

                    alert_msg = f"Sync Statistics\n\n        Epoch: {epoch}\n        Difference: {synced}\n\n{msg}"

                    uptime_res, info_str, uptime = self.check_uptime()
                    alert_msg += f"Uptime Statistics\n\n        Epoch: {epoch}\n        Uptime: {uptime}%\n\nFull Data:\n\n{info_str}"

                    if not uptime_res:
                        problem = True

                    else:
                        self.build_send_error_message(alert_msg)

                    if problem:
                        self.build_send_error_message(alert_msg)
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

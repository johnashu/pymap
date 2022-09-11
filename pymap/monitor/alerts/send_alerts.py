import logging as log
import socket
from pymap.monitor.alerts.alerts_base import AlertsBase
from pymap.monitor.util.tools import check_hours_alert
from pymap.includes.config import alert_envs


class Alerts(AlertsBase):

    hostname = socket.gethostname()

    def build_send_error_message(self, *a, **kw) -> None:
        err_msg = self.build_error_message(*a, **kw)
        self.send_alert(
            f"Node is Behind -- {self.hostname}",
            err_msg,
            "danger",
            log.error,
            f" Node is Behind -- {self.hostname}",
        )

    def build_error_message(self, msg: str, blocks: int, epoch: int):
        try:
            html = f"""<strong>Local Epoch:</strong> {epoch}\n<strong>Difference:</strong> {blocks}\n\n{msg}"""
        except KeyError as e:
            msg = f"Problem Sending alert [ build_error_message ] {e}"
            log.error(msg)
            return msg
        return html

    def generic_error(self, e: str):
        self.send_alert(
            f"Sync Script Error -- {self.hostname}",
            e,
            "danger",
            log.error,
            f"Sending ERROR Alert..ERROR  ::  {e}",
        )

    @check_hours_alert
    def happy_alert(
        self,
        times_sent: dict,
        epoch: int,
        msg: str,
        _send_alert: bool = False,
        first_run: bool = False,
    ) -> dict:

        if alert_envs.FULLY_SYNCED_NOTIFICATIONS and _send_alert:
            self.send_alert(
                f"Epoch: [ {epoch} ] Node is Synced -- {self.hostname}",
                msg,
                "info",
                log.info,
                f"Epoch: [ {epoch} ] Node is Synced -- {self.hostname}",
            )
        return times_sent

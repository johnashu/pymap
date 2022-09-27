import logging as log
import socket
from pymap.monitor.alerts.alerts_base import AlertsBase
from pymap.monitor.util.tools import check_hours_alert
from pymap.includes.config import alert_envs


class Alerts(AlertsBase):

    hostname = socket.gethostname()

    def send_error_message(self, err_msg, epoch, *a, **kw) -> None:
        # err_msg = self.build_error_message(*a, **kw)
        self.send_alert(
            f"Epoch: [ {epoch} ] Problem With Node -- {self.hostname}",
            err_msg,
            "danger",
            log.error,
            f"Epoch: [ {epoch} ] Problem With Node -- {self.hostname}",
        )

    def dict_to_table(self, d: dict) -> str:
        table = """
        <table border="1" class="dataframe">
            <tbody>                
                """
        for k, v in d.items():
            table += f"""
            <tr>
                <td>{k}</td>
                <td>{v}</td>
                </tr>
                """
        table += """
            </tbody>
            </table>
        """
        return table

    def build_html_message(self, msg: str, d: dict = None):
        table = ""
        if d:
            table = self.dict_to_table(d)

        try:
            message = msg.replace("\n", "<br>").replace("\t", "    ")
            html = f"""{message}{table}"""
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

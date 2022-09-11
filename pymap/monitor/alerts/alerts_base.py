import logging as log
from pymap.includes.config import alert_envs
from pymap.monitor.sending.send_email import send_email
from pymap.monitor.includes.monitor_setup import server_hostname


class AlertsBase:
    def __init__(
        self,
        # MAPSTATS_API: str,
        # connect_to_api: object,
        **kwargs,
    ) -> None:
        # self.MAPSTATS_API = MAPSTATS_API
        # self.connect_to_api = connect_to_api
        self.__dict__.update(kwargs)

    def send_to_mapstats(
        self, subject: str, msg: str, alert_type: str, hostname: str = server_hostname
    ) -> None:
        return
        # j = {
        #     "api_token": self.envs.MAPSTATS_TOKEN,
        #     "alert-type": alert_type,
        #     "subject": subject,
        #     "message": msg,
        #     "hostname": hostname,
        # }
        # full, _, _ = self.connect_to_api("", self.MAPSTATS_API, "", j=j)
        # log.info(full)
        # log.info(hostname)

    def send_alert(
        self,
        subject: str,
        msg: str,
        _type: str = "Danger",
        log_level: log = log.info,
        log_msg: str = "[INFO]",
    ) -> None:
        log_level(log_msg)
        if alert_envs.SEND_ALERT_TO_MAPSTATS:
            self.send_to_mapstats(subject, msg, _type)
        if alert_envs.SEND_EMAIL:
            send_email(subject, msg)

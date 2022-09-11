from pymap.includes.config import alert_envs
from pymap.monitor.includes.setup_utils import parse_times

server_hostname = ""
FULLY_SYNCED_NOTIFICATIONS = False
times, times_sent = [], {}

if alert_envs.FULLY_SYNCED_NOTIFICATIONS_PER_DAY > 0:
    FULLY_SYNCED_NOTIFICATIONS_EVERY_X_HOURS = (
        24 / alert_envs.FULLY_SYNCED_NOTIFICATIONS_PER_DAY
    )
    times, times_sent = parse_times(FULLY_SYNCED_NOTIFICATIONS_EVERY_X_HOURS)
    FULLY_SYNCED_NOTIFICATIONS = True

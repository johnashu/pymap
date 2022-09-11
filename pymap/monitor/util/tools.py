from pymap.monitor.includes.monitor_setup import times
import datetime


def check_hours_alert(function_to_decorate):
    def wrapper(
        self, shard, times_sent, _send_alert: bool = False, first_run: bool = False
    ):
        now = datetime.datetime.now()
        h = str(now.hour)
        if not first_run:
            if int(h) in times:
                if not times_sent[h]:
                    times_sent[h] = True
                    _send_alert = True
            if all([times_sent[x] for x in times_sent]):
                times_sent = {str(x): False for x in times}
        else:
            _send_alert = True

        return function_to_decorate(
            self, shard, times_sent, _send_alert=_send_alert, first_run=first_run
        )

    return wrapper

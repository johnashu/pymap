from pymap.includes.config import envs
from pymap.monitor.monitor import Monitor

from_env = envs.__dict__


def test_alert() -> None:
    msg = f"""
        Local Block Number: 123312
        RPC Block Number:   123213       
        """
    m.happy_alert(
        {},
        27,
        f"        Epoch: 27\n        Difference: 5\n{msg}",
        first_run=True,
    )


if __name__ == "__main__":
    m = Monitor(**from_env)
    m.start_monitor()

    # print(m.check_peers())

    # test_alert()
    # m.setup_monitor_service()

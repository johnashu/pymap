from code import interact
from pymap.includes.config import envs
from pymap.monitor.monitor import Monitor

from_env = envs.__dict__

if __name__ == "__main__":

    m = Monitor(**from_env)
    m.start_monitor()

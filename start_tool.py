from pymap.includes.config import envs
from pymap.interactive.interactive import InteractiveSetup

from_env = envs.__dict__

if __name__ == "__main__":

    i = InteractiveSetup(**from_env)
    i.start()

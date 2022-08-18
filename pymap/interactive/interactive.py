from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields
from pymap.interactive.menu import Menu

from_env = envs.__dict__
print(from_env)


class InteractiveSetup(Menu):
    def __init__(self, **base_fields: dict) -> None:
        super(InteractiveSetup, self).__init__(**base_fields)

    def start(self) -> None:
        self.intro_message()
        self.run_full_node()

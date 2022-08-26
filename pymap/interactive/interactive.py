from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields
from pymap.interactive.menu import Menu
from pymap.tools.key_from_keystore import pk_from_store

from_env = envs.__dict__
print(from_env)


class InteractiveSetup(Menu):
    def __init__(self, **base_fields: dict) -> None:
        super(InteractiveSetup, self).__init__(**base_fields)

    def find_pk(self) -> None:
        context = {"keystore": self.keystore, "password": self.password}
        context.update(self.handle_input(context))
        pk_from_store(self.keystore, self.password)

    def start(self) -> None:
        self.intro_message()
        self.run_full_node()

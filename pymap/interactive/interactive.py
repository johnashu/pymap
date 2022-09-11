from pymap.interactive.menu import Menu
from pymap.tools.general import General


class InteractiveSetup(Menu, General):
    def __init__(self, **base_fields: dict) -> None:
        super(InteractiveSetup, self).__init__(**base_fields)

    def start(self) -> None:
        self.intro_message()
        self.run_full_node()

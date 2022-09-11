import os
from pymap.tools.key_from_keystore import pk_from_store
from pymap.tools.block_epoch_utils import time_to_next_block
from pymap.includes.templates.systemd import monitorService
from pymap.tools.create_service import create_systemd


class General:
    def __init__(self, reset: int = 0, **kw):
        super(General, self).__init__()

    def backup_env(self) -> None:
        fn = input(
            "Please Enter Backup Location and Filename, i.e. /home/backup.env : "
        )
        self.update_env(self.base_field_keys, fn)

    def find_pk(self) -> None:
        context = {"keystore": self.keystore, "password": self.password}
        context.update(self.handle_input(context))
        pk_from_store(self.keystore, self.password)

    def display_and_update_env(self) -> None:
        while 1:
            os.system("clear")
            cur_list = self.list_envs()
            try:
                choice = int(
                    input(
                        "\nTo update an item, please select a number or press 0 to go back:  "
                    )
                )
                if choice == 0:
                    break
                elif choice == 99:
                    self.backup_env()
                else:
                    self.handle_input({cur_list[choice]: str()}, allow_empty=True)
            except ValueError:
                self.error_input()

    def compare_block_numbers(self) -> tuple:
        self.get_eth_block_number_from_node()
        rpc_block = int(self.get_block_number())
        local_block = int(self.local_block)
        match = local_block == rpc_block
        msg = f"""
        Local Block Number: {local_block}
        RPC Block Number:   {rpc_block}       
        """
        synced = f"Blocks Synced:      {self.red_or_green(match)} "
        print(self.star_surround(msg + synced))
        return match, rpc_block, local_block, msg

    def get_epoch_data(self) -> None:
        current_block = int(self.get_block_number())
        bpe = int(self.blocks_per_epoch)
        t, epoch, next_epoch = time_to_next_block(current_block, bpe)
        msg = f"""
        Current Block: {current_block}

        Current Epoch: {epoch}
        
        Next Epoch:    {epoch+1} starts @ block {next_epoch} in {t.days} day(s) | {t.hours} hour(s) | {t.minutes} min(s) | {t.seconds} sec(s)
        """
        print(self.star_surround(msg))
        return epoch

    def setup_monitor_service(
        self,
        context: dict = {"working_dir": str()},
    ) -> None:
        context.update(self.handle_input(context))

        create_systemd(
            context, template=monitorService, serviceName="atlasMonitorService"
        )

        commands = (
            "sudo service atlasMonitorService stop",
            "sudo systemctl daemon-reload ",
            "sudo chmod 644 /etc/systemd/system/atlasMonitorService.service",
            "sudo systemctl enable atlasMonitorService.service",
            "sudo service atlasMonitorService start",
        )

        for cmd in commands:
            self.run_method(
                cmd.split(),
                {},
                prog="",
            )

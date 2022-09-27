from typing import Type
from colorama import Style, Fore, Back
from pymap.tools.file_op import open_file
from pymap.includes.mappings.menu_str import menu_items
from pymap.includes.config import envs
from pymap.tools.utils import readable_price


class PrintStuff:
    def __init__(self, isMenu: bool = True, **kw):
        self.print_stars = "*" * 93
        self.reset_stars = self.print_stars + Style.RESET_ALL
        super(PrintStuff, self).__init__()

    def stars(self, reset=0) -> None:
        p = self.print_stars
        if reset:
            p = self.reset_stars
        print(p)

    def string_stars(self, reset=0) -> str:
        p = self.print_stars
        if reset:
            p = self.reset_stars
        return p

    def whitespace(self) -> None:
        print("\n" * 2)

    def intro_message(self):
        p = f"""
        {self.string_stars()}
            ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗                
            ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗               
            ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║               
            ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║               
            ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝               
            ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝                
                                                                                                            
            ███╗   ███╗ █████╗ ██████╗     ██████╗ ██████╗  ██████╗ ████████╗ ██████╗  ██████╗ ██████╗ ██╗     
            ████╗ ████║██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██╔════╝██╔═══██╗██║     
            ██╔████╔██║███████║██████╔╝    ██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║██║     ██║   ██║██║     
            ██║╚██╔╝██║██╔══██║██╔═══╝     ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██║   ██║██║     ██║   ██║██║     
            ██║ ╚═╝ ██║██║  ██║██║         ██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗╚██████╔╝███████╗
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
                                                                                                            
            ██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗ ██████╗ ██████╗                              
            ██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗                             
            ██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║   ██║██████╔╝                             
            ╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗                             
            ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║                             
            ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                             
                                                                                                            
            ███████╗███████╗████████╗██╗   ██╗██████╗                                                          
            ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗                                                         
            ███████╗█████╗     ██║   ██║   ██║██████╔╝                                                         
            ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝                                                          
            ███████║███████╗   ██║   ╚██████╔╝██║                                                              
            ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝             
                                                
        {self.string_stars()}
        
        """
        print(p)

    def display_from_file(self, fn) -> None:
        print(Style.RESET_ALL)
        for x in open_file(fn):
            x = x.strip()
            try:
                x = eval(x)
            except SyntaxError:
                pass
            if x:
                print(x)

    def error_input(self) -> None:
        self.whitespace()
        self.stars(reset=1)
        print(
            "* "
            + Fore.RED
            + "WARNING"
            + Style.RESET_ALL
            + ": Only numbers are possible, please try your selection again."
        )
        self.stars(reset=1)
        self.whitespace()
        input("* Press ENTER to return to the menu")

    def create_menu(self):
        msg = (
            Fore.YELLOW
            + Back.RED
            + "WARNING: You may miss blocks during a reboot!"
            + Style.RESET_ALL
        )
        print("*  Menu Options:")
        print("*")
        for i, k in enumerate(menu_items.keys()):
            print(f"*  [{i+1:>2}] {k}")
            self.menu[i + 1] = eval(f"self.{menu_items[k]}")
        msg = f"""*  [999] Reboot Server             - {msg}
*  [0] Exit Application            - Goodbye!
"""
        self.star_surround(msg)

    def list_envs(self) -> None:
        ignore = ("envFile",)
        c = 1
        cur_list = {}
        back = "*  " + Fore.GREEN + "[ 0] - Back To Main Menu" + Style.RESET_ALL
        backup = "*  " + Fore.GREEN + "[99] - Backup Env to file" + Style.RESET_ALL
        for k, v in self.__dict__.items():
            if k in envs.__dict__.keys() and k not in ignore:
                cur_list[c] = k
                print(f"* [{c:>2}] - {k:<20}  ::  {v}")
                c += 1
        msg = f"{back}\n{backup}"
        self.star_surround(msg)
        return cur_list

    def star_surround(self, msg) -> None:
        print(f"\n{self.print_stars}\n\n{msg}\n\n{self.print_stars}")

    def red_or_green(self, check) -> str:
        if check:
            return "" + Fore.GREEN + str(check) + Style.RESET_ALL
        return "" + Fore.RED + str(check) + Style.RESET_ALL

    def get_max_length_of_text(self, d: dict) -> int:
        max_len = 0
        for k, v in d.items():
            try:
                x = len(k)
                if x > max_len:
                    max_len = x
            except TypeError:
                continue

        return max_len

    def display_dict(
        self, items: list, meta: dict = {}, ignore: tuple = (), show: bool = True
    ) -> None:
        """
        Expects a list of dictionaries to display.
        meta should contain {name: (pre, post, readable price)} - i.e.
        {"voteReward": (None, '%', True)}
        """
        # Items to multiply by 100 to create a proper % of 100%
        mulitply = ("voteReward",)
        rtn_str = ""
        rtn_dict = {}
        if not items:
            return False, rtn_str

        for d in items:
            c = self.get_max_length_of_text(d)
            msg = ""
            for k, v in d.items():
                if k in ignore:
                    continue

                if not v:
                    v = "None"

                if k in mulitply:
                    v = int(v) * 100

                pre, post, readable, kw = (
                    meta.get(k) if meta.get(k) else ("", "", False, {})
                )
                pre = pre if pre else ""
                post = post if post else ""

                if readable:
                    kwargs = {**{"num": v}, **kw} if kw else {"num": v}
                    v = readable_price(**kwargs) if readable else v

                if post == "%":
                    v = round(float(v), 2)
                v = f" {pre} {v}{post}"

                msg += f"{k:<{c}} :: {v:<{c}}\n"
                rtn_dict[k] = v

            if show:
                self.star_surround(msg)
            rtn_str += msg
        return True, rtn_str, rtn_dict

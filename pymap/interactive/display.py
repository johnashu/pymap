from colorama import Style, Fore, Back
from pymap.tools.file_op import open_file
from pymap.includes.mappings.menu_str import menu_items


class PrintStuff:
    def __init__(self, **kw):
        self.print_stars = "*" * 93
        self.reset_stars = self.print_stars + Style.RESET_ALL
        self.menu = {
            0: self.finish_node,
            999: self.reboot_server,
        }
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
            + ": Only numbers are possible, please try your selection on the main menu once again."
        )
        self.stars(reset=1)
        self.whitespace()
        input("* Press ENTER to return to the main menu")

    def create_menu(self):
        msg = (
            Fore.YELLOW
            + Back.RED
            + "WARNING: You may miss blocks during a reboot!"
            + Style.RESET_ALL
        )
        print("*  Map Validator Menu Options:")
        print("*")
        for i, k in enumerate(menu_items.keys()):
            print(f"*  [{i+1}] {k}")
            self.menu[i + 1] = eval(f"self.{menu_items[k]}")
        print(
            f"""
        
*********************************************************************************************
print("*  [999] Reboot Server             - {msg}
print("*  [0] Exit Application            - Goodbye!")
*********************************************************************************************
        """
        )


# whitespace = PrintStuff.whitespace
# stars = PrintStuff().stars
# string_stars = PrintStuff().string_stars
# stars_reset = PrintStuff(reset=1).stars
# string_stars_reset = PrintStuff(reset=1).string_stars

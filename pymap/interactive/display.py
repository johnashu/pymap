from colorama import Style, Fore, Back
from pymap.tools.file_op import open_file


class PrintStuff:
    def __init__(self, **kw):
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

    @classmethod
    def whitespace(self) -> None:
        print("\n" * 8)

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


# whitespace = PrintStuff.whitespace
# stars = PrintStuff().stars
# string_stars = PrintStuff().string_stars
# stars_reset = PrintStuff(reset=1).stars
# string_stars_reset = PrintStuff(reset=1).string_stars

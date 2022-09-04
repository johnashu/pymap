from decimal import Decimal, ROUND_DOWN
import logging as log
import re


def camel_to_snake(string):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()


def round_down(amount: str, decimals: int) -> float:
    places = f'.{"".join(["0" for _ in range(decimals)])}'
    rounded = Decimal(amount).quantize(Decimal(places), rounding=ROUND_DOWN)
    return float(rounded)


def readable_price(num, d: int = 18, show_decimals=True, print_res=True) -> str:
    temp = []
    c = 1
    try:
        main, decimals = f"{int(num) / 10 ** d:.{d}f}".split(".")
    except ValueError:
        return float(num)

    for d in reversed(main):
        temp.insert(0, d)
        if c == 3:
            temp.insert(0, ",")
            c = 1
        else:
            c += 1

    if not show_decimals:
        decimals = ""

    rtn_str = "".join(temp)
    rtn_str += f".{decimals}" if show_decimals else ""
    if rtn_str[0] == ",":
        rtn_str = rtn_str[1:]

    if print_res:
        log.info(rtn_str)
    return rtn_str


def askYesNo(question: str) -> bool:
    YesNoAnswer = ""
    while not YesNoAnswer.startswith(("Y", "N")):
        YesNoAnswer = input(f"{question} - yes / no): ").upper()
    if YesNoAnswer.startswith("Y"):
        return True
    return False


def is_signer() -> bool:
    return askYesNo("Is Signer Account? ")


def take_input(_type: object, msg: str) -> None:
    while True:
        p = True
        _in = input(msg)
        if not _in:
            break
        try:
            _type(_in)
        except ValueError:
            print(f"\n\tPlease Enter input of type [ {_type.__name__.title()} ] \n")
            p = False
        if p:
            break
    return _in

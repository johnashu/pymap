import logging
import sys, os, datetime


def start_logger(verbose: bool = False) -> logging:
    ts = datetime.datetime.now()
    # LOGGING
    file_handler = logging.FileHandler(
        os.path.join(
            "logs", f"{ts.day}-{ts.month}-{ts.year}_{ts.hour}_{ts.minute}.log"
        ),
        "a",
        "utf-8",
    )

    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, stdout_handler]

    # <%(funcName)s>
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=handlers,
        datefmt="%d-%m-%Y %H:%M:%S",
    )

    # disable external Logging (imported modules.)
    if not verbose:
        for v in logging.Logger.manager.loggerDict.values():
            v.disabled = True

    return logging.getLogger(__name__)

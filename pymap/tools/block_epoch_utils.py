from math import floor
import datetime
from collections import namedtuple


def normalise_seconds(seconds: int) -> tuple:
    (days, remainder) = divmod(seconds, 86400)
    (hours, remainder) = divmod(remainder, 3600)
    (minutes, seconds) = divmod(remainder, 60)
    return namedtuple("_", ("days", "hours", "minutes", "seconds"))(
        days, hours, minutes, seconds
    )


def get_current_epoch(current_block, blocks_per_epoch) -> int:
    calc = (current_block - 1) / blocks_per_epoch
    epoch = floor(calc) + 1
    return epoch


def time_to_next_block(current_block, blocks_per_epoch) -> datetime:
    # TODO: Get Block Time from API if possible
    block_time = 4.5  # seconds
    epoch = get_current_epoch(current_block, blocks_per_epoch)
    next_epoch = (epoch * blocks_per_epoch) + 1
    blocks_to_next_epoch = next_epoch - current_block
    seconds_to_next_epoch = floor(block_time * blocks_to_next_epoch)
    return normalise_seconds(seconds_to_next_epoch), epoch, next_epoch

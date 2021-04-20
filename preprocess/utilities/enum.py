from functools import partial
from enum import IntEnum, Enum
from .file_writers import write_to_csv, write_to_json


def do_nothing(foo: any) -> None:
    pass

class Interval(IntEnum):
    seconds = 1
    minutes = 60
    hours = 3600
    days = 25200
    weeks = 604800
    months = 2592000


class Print_to_File(Enum):
    none = partial(do_nothing)
    csv = partial(write_to_csv)
    json = partial(write_to_json)

    def __call__(self, *args):
        self.value(*args)


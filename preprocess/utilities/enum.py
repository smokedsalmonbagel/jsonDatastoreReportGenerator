from functools import partial
from enum import IntEnum, Enum
from .file_writers import write_to_csv, write_to_json


def do_nothing(foo: any) -> None:
    pass

class Interval(IntEnum):
    minutes = 1
    hours = 60
    days = 1440
    weeks = 10080
    months = 43200


class Print_to_File(Enum):
    none = partial(do_nothing)
    csv = partial(write_to_csv)
    json = partial(write_to_json)

    def __call__(self, *args):
        self.value(*args)


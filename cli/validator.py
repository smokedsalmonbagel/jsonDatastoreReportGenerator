import datetime
from .errors import IncompatibleDatesError, InvalidDateError, InvalidIntervalError


class Validator():
    def __init__(self, start: str, end: str, interval: str, duration: int, fields: list, fmt: any):
        self.__start = start
        self.__end = end
        self.__interval = interval
        self.__duration = duration
        self.__fields = fields
        self.__fields.insert(0, "pitime")
        self.__fmt = fmt

    def validate(self):
        is_start_valid = self.__is_Valid_Date(self.__start)
        is_end_valid = self.__is_Valid_Date(self.__end)
        is_interv_valid = self.__is_Valid_Interval(self.__interval)

        if is_start_valid > is_end_valid:
            raise IncompatibleDatesError(is_start_valid, is_end_valid)

        result = {
            "start date": is_start_valid,
            "end date": is_end_valid,
            "interval": is_interv_valid,
            "count": self.__duration,
            "fields": self.__fields,
            "output_format": self.__fmt
        }

        return result

    @staticmethod
    def __is_Valid_Date(date):
        try:
            date_obj = datetime.datetime.strptime(date, "%Y%m%dT%H%M%S")
        except:
            raise InvalidDateError()

        return date_obj

    @staticmethod
    def __is_Valid_Interval(interval):
        allowed_terms = {'sec': 'seconds', 'min': 'minutes',
                         'hr': 'hours', 'dy': 'days', 'wk': 'weeks', 'mnt': 'months'}

        if interval in allowed_terms.keys():
            return allowed_terms[interval]
        else:
            raise InvalidIntervalError()

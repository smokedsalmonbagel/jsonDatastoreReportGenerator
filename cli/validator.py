import datetime
from .errors import IncompatibleDatesError, InvalidDateError, InvalidIntervalError


class Validator():
    def __init__(self, cli_obj: dict):
        self.__start = cli_obj["start_date"]
        self.__end = cli_obj["end_date"]
        self.__interval = cli_obj["interval"]
        self.__duration = cli_obj["duration"]
        self.__fields = cli_obj["fields"]
        self.__fields.insert(0, "pitime")
        self.__fmt = cli_obj["format_"]
        self.__dir = cli_obj["location"].replace("\\", "/")

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
            "output_format": self.__fmt,
            "location": self.__dir
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

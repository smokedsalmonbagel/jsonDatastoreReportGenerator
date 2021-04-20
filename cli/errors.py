class IncompatibleDatesError(Exception):
    def __init__(self, start_date, end_date):
        self.start_date = start_date.strftime("%m-%d-%Y")
        self.end_date = end_date.strftime("%m-%d-%Y")


    def __str__(self):
        return "{} is not earlier than {}. Please check again".format(self.start_date, self.end_date)


class InvalidDateError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "Invalid date supplied"


class InvalidIntervalError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "Invalid interval supplied. It should be 'sec', 'min', 'hr', 'wk' or 'mnt'"

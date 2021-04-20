class DateNotFoundError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return self.message
        else:
            return "It appears that there are no logs for the date requested. Please supply two valid dates"

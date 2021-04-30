from .utilities import bin_search, get_files


class Preprocess():
    def __init__(self, obj: dict) -> None:
        self.start = obj['start date']
        self.end = obj['end date']
        self.interv = obj['interval']
        self.__dir = obj['location']

    def __stringify(self) -> None:
        start = self.start.strftime("%Y%m%dT%H%M%S")
        end = self.end.strftime("%Y%m%dT%H%M%S")
        self.dates = (start.replace("T", "_"), end.replace("T", "_"))

    def __get_search_terms(self) -> None:
        file_list = get_files(self.__dir)
        start_date = self.dates[0]
        end_date = self.dates[1]

        start_index, end_index = bin_search(
            file_list, start_date), bin_search(file_list, end_date)
        self.search_indexes = (start_index, end_index)
        self.file_list = file_list[start_index:end_index + 1]

    def get_search_list(self) -> list:
        self.__stringify()
        self.__get_search_terms()
        return self.file_list

import os, json
from preprocess import Interval, Print_to_File
from functools import reduce
from operator import add
from datetime import datetime


class Parser():
    def __init__(self, file_list: list, data: dict) -> None:
        self.__file_list = file_list
        self.__interv = data['interval']
        self.__count = data['count']
        self.__fields = data['fields']
        self.__fmt = data['output_format']
        self.__store = {x: [] for x in self.__fields}
        self.__mutated = self.__reformat()
        
        self.__result = {
            "code": 1,
            "message": "success",
            "interval": self.__interv,
            "duration": self.__count,
            "data": self.__mutated
        }
        
        self.out = json.dumps(self.__result)
        self.__print_to_file(self.__fmt, self.__result)


    def __load_data(self):
        files = [self.__get_file_name(f) for f in self.__file_list]

        for file_ in files:
            with open(file_, 'r') as f:
                lines = f.readlines()
                yield(lines)


    def __get_file_name(self, file_name: str):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'logs/' + file_name)
        filename = os.path.abspath(os.path.realpath(filename))
        return filename

    
    def __resample(self):
        fields_data = self.__store
        all_data = self.__load_data()

        for jsons_ in all_data:
            for json_ in jsons_:
                json_data = json.loads(json_)
                
                if json_data["type"] == "print_reading":
                    [fields_data[x].append(json_data[x]) if x in json_data else fields_data[x].append("None") for x in self.__fields]

        self.__resampled = fields_data

    
    def __segments(self):
        self.__resample()
        factor_ = Interval[self.__interv].value
        counter = self.__count
        length = factor_ * counter
        data = self.__resampled
        
        for field in self.__fields:
            dat = data[field]
            segments = [dat[x: x+factor_] for x in range(0, length, factor_)]
            yield({
                field: segments
            })


    def __reformat(self):
        segments = self.__segments()
        temp = {x: [] for x in self.__fields}

        for field in segments:
            for key, items in field.items():
                n = [self.__mean(list(self.__valid_num(x))) if key != "pitime" else self.__stringify_timestamp(self.__timestamp_mean(x)) for x in items]
                temp[key] = n
                
        return temp

    
    @staticmethod
    def __mean(arr: list) -> float:
        result = sum(arr) / len(arr)
        result = round(result, 2)
        return result

    
    @staticmethod
    def __timestamp_mean(arr: list) -> float:
        arr = [datetime.fromisoformat(x) for x in arr]
        min_timestamp = min(arr)
        deltas = [x - min_timestamp for x in arr]

        ave_timestamp = min_timestamp + reduce(add, deltas) / len(deltas)
        return ave_timestamp

    
    @staticmethod
    def __stringify_timestamp(date_obj):
        return date_obj.strftime("%Y-%m-%dT%H:%M:%S")



    @staticmethod
    def __valid_num(inp):
        return filter(lambda x: str(x).isnumeric(), inp)


    @staticmethod
    def __print_to_file(fmt, data):
        if fmt is not None:
            Print_to_File[fmt](data)

            
        

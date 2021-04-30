import time

from cli import cli_parser
from log_parse import Parser
from preprocess import Preprocess

if __name__ == '__main__':
    start = time.time()
    validated_data = cli_parser()
    preprocess_obj = Preprocess(validated_data)
    search_list = preprocess_obj.get_search_list()

    my_parser = Parser(search_list, validated_data)
    total_time = round(time.time() - start, 2)
    
    print("completed in {} seconds".format(total_time))
    print(my_parser.out)


from cli import cli_parser
from log_parse import Parser
from preprocess import Preprocess


"""
    python app.py -P min -D 20 -S 20190102T010319 -E 20190104T165909 -F adc_67_max,adc_67_min,elec_6_sum
"""

if __name__ == '__main__':
    validated_data = cli_parser()
    preprocess_obj = Preprocess(validated_data)
    search_list = preprocess_obj.get_search_list()

    my_parser = Parser(search_list, validated_data)
    print(my_parser.out)


#! /usr/bin/env python
import argparse
from .validator import Validator


def cli_parser():
    # Create the parser
    m_parser = argparse.ArgumentParser(
        prog="report generator", description='create a summary report for a specific duration over a specified intervals')

    # Add the arguments
    m_parser.add_argument('--Start', '-S',
                          #   metavar='start date',
                          type=str, action='store',
                          help='the start date in the format MM/DD/YYYY', required=True)

    m_parser.add_argument('--End', '-E',
                          #   metavar='end date',
                          type=str, action='store',
                          help='the end date in the format MM/DD/YYYY', required=True)

    m_parser.add_argument('--Period', '-P',
                          choices=['sec', 'min', 'hr', 'dy', 'wk', 'mnt'],
                          type=str, required=True, action='store',
                          help='formats the data in minutes [mins], hours [hr], days [dy] weeks [wk] or months [mnt]')

    m_parser.add_argument('--Duration', '-D',
                          type=int, required=True, action='store',
                          help='quantity of time you want')

    m_parser.add_argument('--Fields', '-F',
                          type=str, required=True, action='store',
                          help='list of fields you are interested in')

    m_parser.add_argument('--Location', '-L',
                          type=str, required=True, action='store',
                          help='full directory of the location where the log files are stored')

    m_parser.add_argument('--Out', '-O',
                          choices=['csv', 'json'],
                          type=str, required=False, action='store',
                          help='choose to write output to file - [csv], [json]')

    # Execute the parse_args() method
    args = m_parser.parse_args()
    fields = args.Fields.split(",")
    location = args.Location
    start_date, end_date  = args.Start, args.End
    interval, duration, format_ = args.Period, args.Duration, args.Out

    cli_obj = {
        "start_date": start_date,
        "end_date": end_date,
        "interval": interval,
        "duration": duration,
        "fields": fields,
        "format_": format_,
        "location": location
    }

    m_validator = Validator(cli_obj)
    validated = m_validator.validate()

    return validated

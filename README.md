# JSON DATASTORE REPORT GENERATOR

This is a CLI tool for resampling data in log files and generating report based on user specifications. It works primarily by collecting data from log files, parsing and aggregating the data to suit user specified format. The data is aggregated using arithmetric mean of data over a specified duration.

## Usage

Download the entire folder and put all your log files in `./logs`. CD into the root directory and run the following code. The [-O] flag is optional and is only used if you wish to have an output file.

```
    python app.py -P [interval] -D [duration] -S [start date] -E [end date] -F [fields of interests] -O [json/csv]
```

For help use `python app.py --help`

## Libraries and Modules

- argparse
- datetime
- json
- os
- sys
- csv
- enum (Enum, IntEnum)
- functools (partial, reduce)
- operator (add)

## Data

The scripts assumes the following:

- Data is in log files that are collocated with the program code.

- The log files are New Line Delimited JSON (ndjson).

- Data is logged on the average per second.

- Rows of data containing fileds of interest are dictionaries and must have the property `row['type'] == 'print_reading'`.

- The timestamp for each row is in ISO format.

## Aggregation and Missing Data

The script collects data for specified fields starting and ending at user specified dates. If it finds data to be missing for a field on any date, it simply returns `'None'`. It then creates `[-D]` segments of length corresponding to `[-P]`. Because, the script anticipates data logged per second, `P == min` means segments of lenth, 60 and `P == hr` means segments of length, 3600. The script then omits `'None'` values in each segment and returns the aritmetic mean of all the values in the segment. All results are returned as 2 decimal floats.

## Output

The script optionally writes an output file of file extension `[-O == json | csv]`. The json schema is:

```
{
    "code": integer,
    "message": string,
    "interval": string,
    "duration": integer,
    "data": dictionary,
    "time stamps": list
}
```

The schema for the csv output is:

|     Time    | [Fields] |
| ----------- | -------- |
| time stamps | values   |


# JSON DATASTORE REPORT GENERATOR

This is a CLI tool for resampling data in log files and generating report based on user specifications. It works primarily by collecting data from log files, parsing and aggregating the data to suit user specified format. The data is aggregated using arithmetric mean of data over a specified duration.

## Usage

Download the entire folder. CD into the root directory and run the following code. The [-O] flag is optional and is only used if you wish to have an output file.

```
    python app.py -P [interval] -D [duration] -S [start date] -E [end date] -F [fields of interests] -O [json/csv] -L [location of logs]
```

For example:

```
    python app.py -P min -D 20 -S 20190102T010319 -E 20190104T165909 -F adc_67_max,adc_67_min,elec_6_sum -O json -L C:\Users\...\logs
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

- Data is logged averagely every minute.

- Rows of data containing fileds of interest are dictionaries and must have the property `row['type'] == 'print_reading'`.

- The timestamp for each row is in ISO format.

- All the log files can be found in the root fo the supplied location [-L]. The script does not search for sub directories

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


## Benchmark Tests

Available log files were used to test the program and the results are shown in the table below.

| Interval | Duration | Span | Result |
|--------- | -------- | --------- | ------ |
| hours | 3 | 3 days | 0.45 seconds |
| hours | 70 | 3 days | 0.49 seconds |
| days | 3 | 3 days | 0.22 seconds |
| hours | 312 | 17 days | 2.87 seconds |
| days | 16 | 17 days | 1.92 seconds |
| weeks | 2 | 17 days | 2.43 seconds


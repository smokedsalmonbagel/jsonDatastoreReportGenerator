import csv, json, os

def write_to_json(data: dict):
    json_data = json.dumps(data, indent = 4)

    with open("output/output.json", "w") as f:
        f.write(json_data)


def write_to_csv(data: dict):
    obj = data['data']
    column_names = [key for key in obj.keys()]
    column_names.remove("pitime")
    column_names.insert(0, "timestamp")
    counter = data['duration']

    with open("output/output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=column_names)
        row_writer = csv.writer(f)
        writer.writeheader()

        for i in range(counter):
            write_data = [items[i] for _, items in obj.items()]
            row_writer.writerow(write_data)


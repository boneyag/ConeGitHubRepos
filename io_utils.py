import json



def write_to_json(json_obj, file_name):
    with open(f"{file_name}.json", 'w') as f:
        json.dump(json_obj, f, default=vars)


def read_from_json(file_name):
    with open(f"{file_name}.json") as f:
        json_obj = json.load(f)

    return json_obj
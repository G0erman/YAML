import yaml

def parse_data(path: str):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data

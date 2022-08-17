import os
from os.path import join, exists

paths = dict(
    json_in=join("IN", "JSON"),
    csv_in=join("IN", "CSV"),
    json_out=join("OUT", "JSON"),
    csv_out=join("OUT", "CSV"),
)

json_in = join("data", paths["json_in"])
csv_in = join("data", paths["csv_in"])
json_out = join("data", paths["json_out"])
csv_out = join("data", paths["csv_out"])


def create_data_path(pth: str, data_path: str = "data") -> str:
    cwd = os.getcwd()
    p = join(cwd, data_path, pth)
    if not exists(p):
        os.mkdir(p)
    return p


create_data_path("", data_path="logs")
create_data_path("", data_path="data")

for _, p in paths.items():
    create_data_path(p.split("\\")[0], data_path="data")
    create_data_path(p, data_path="data")

import json, csv
import logging as log


def open_file(fn: str) -> list:
    with open(fn, "r") as f:
        return f.read()


def save_file(fn: str, data: list) -> list:
    with open(fn, "w") as f:
        return f.write(data)


def open_json(fn: str) -> json:
    with open(f"{fn}.json", "r", encoding="utf-8") as j:
        return json.load(j)


def save_json(fn: str, d: dict) -> json:
    with open(f"{fn}.json", "w", encoding="utf-8") as j:
        json.dump(d, j, indent=4, ensure_ascii=False)
        log.info(f"File - {fn}.json Created")


def open_csv(fn: str) -> dict:
    with open(f"{fn}.csv", "r", newline="", encoding="utf-8") as csvfile:
        r = csv.DictReader(csvfile, delimiter=",")
        return list(r)


def save_csv(fn: str, data: list, header: list, inc: int = 1) -> None:
    try:
        with open(f"{fn}.csv", "w", newline="", encoding="utf-8") as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=header, delimiter=",")
            w.writeheader()
            for x in data:
                w.writerow(x)
    except PermissionError:  # file is open, rename and try again.
        save_csv(f"{fn}-{inc}", data, header, inc=inc + 1)

    log.info(f"File - {fn}.csv Created")

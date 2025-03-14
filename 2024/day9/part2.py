def main() -> int:
    disk_map = parse_input()
    disk_layout = build_disk_layout(disk_map)
    compress(disk_layout)

    return checksum(disk_layout)


def parse_input() -> list:
    with open("input.txt", "r") as f:
        return [int(n) for n in f.read().strip()]


def build_disk_layout(disk_map: list) -> dict:
    layout = {"last_id": -1, "slots": [], "free": [], "used": []}

    for i, num in enumerate(disk_map):
        is_file = bool(not i % 2)

        if is_file:
            layout["last_id"] += 1
            file_id = layout["last_id"]
            layout["used"].append({"start": len(layout["slots"]), "len": num})
            layout["slots"].extend([file_id] * num)
        else:
            if num > 0:
                layout["free"].append({"start": len(layout["slots"]), "len": num})
            layout["slots"].extend(["."] * num)

    return layout


def find_first_empty(disk_layout: dict) -> int:
    try:
        first_empty = disk_layout["slots"].index(".")
    except ValueError:
        first_empty = -1

    return first_empty


def compress(disk_layout: dict) -> None:
    for used_block in disk_layout["used"][::-1]:
        size = used_block["len"]

        for free_block in disk_layout["free"]:
            if free_block["start"] > used_block["start"]:
                continue

            if size <= free_block["len"]:
                break

        else:
            continue

        disk_layout["slots"][free_block["start"] : free_block["start"] + size] = (
            disk_layout["slots"][used_block["start"] : used_block["start"] + size]
        )
        disk_layout["slots"][used_block["start"] : used_block["start"] + size] = [
            "."
        ] * size
        free_block["len"] -= size
        free_block["start"] += size


def checksum(disk_layout: dict) -> None:
    sum_ = 0

    for i, id_ in enumerate(disk_layout["slots"]):
        if id_ == ".":
            continue

        sum_ += i * id_

    return sum_


if __name__ == "__main__":
    print(main())

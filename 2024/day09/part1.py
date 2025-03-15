def main() -> int:
    disk_map = parse_input()
    disk_layout = build_disk_layout(disk_map)
    compress(disk_layout)

    return checksum(disk_layout)


def parse_input() -> list:
    with open("input.txt", "r") as f:
        return [int(n) for n in f.read().strip()]


def build_disk_layout(disk_map: list) -> dict:
    layout = {"last_id": -1, "slots": [], "first_empty": -1}

    for i, num in enumerate(disk_map):
        is_file = bool(not i % 2)

        if is_file:
            layout["last_id"] += 1
            file_id = layout["last_id"]
            layout["slots"].extend([file_id] * num)
        else:
            if layout["first_empty"] == -1:
                layout["first_empty"] = len(layout["slots"])

            layout["slots"].extend(["."] * num)

    return layout


def find_first_empty(disk_layout: dict) -> int:
    try:
        first_empty = disk_layout["slots"].index(".")
    except ValueError:
        first_empty = -1

    return first_empty


def compress(disk_layout: dict) -> None:
    if disk_layout["first_empty"] == -1:
        return

    slots = disk_layout["slots"]
    i = len(slots) - 1

    for data in slots[::-1]:
        if data == ".":
            i -= 1
            continue

        first_empty = disk_layout["first_empty"]

        if first_empty >= i:
            break

        slots[first_empty], slots[i] = slots[i], slots[first_empty]
        disk_layout["first_empty"] = find_first_empty(disk_layout)
        i -= 1


def checksum(disk_layout: dict) -> None:
    sum_ = 0

    for i, id_ in enumerate(disk_layout["slots"]):
        if id_ == ".":
            continue

        sum_ += i * id_

    return sum_


if __name__ == "__main__":
    print(main())

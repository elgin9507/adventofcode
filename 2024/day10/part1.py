from collections import defaultdict


def main() -> int:
    map_data = parse_input()
    trailheads = defaultdict(set)

    for i, row in enumerate(map_data):
        for j, height in enumerate(row):
            if height == 0:
                wander(map_data, (i, j), (i, j), trailheads)

    sum_ = 0

    for start, ends in trailheads.items():
        sum_ += len(ends)

    return sum_


def parse_input(file_path: str = "input.txt") -> list[list[int]]:
    map_data = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            row = [int(x) for x in line]
            map_data.append(row)

    return map_data


def wander(
    map_data: list[list[int]],
    start_loc: tuple[int],
    current_loc: tuple[int],
    trailheads: dict,
) -> None:
    x, y = current_loc
    current_height = map_data[x][y]

    if current_height == 9:
        trailheads[start_loc].add(current_loc)
        return

    up = (x - 1, y)
    right = (x, y + 1)
    down = (x + 1, y)
    left = (x, y - 1)

    for loc in [up, right, down, left]:
        if not within_bounds(map_data, loc):
            continue

        loc_height = map_data[loc[0]][loc[1]]

        if loc_height - current_height == 1:
            wander(map_data, start_loc, loc, trailheads)


def within_bounds(map_data: list[list[int]], loc: tuple[int]) -> bool:
    x, y = loc
    max_x, max_y = len(map_data), len(map_data[0])

    return x in range(max_x) and y in range(max_y)


if __name__ == "__main__":
    print(main())

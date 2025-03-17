from collections import defaultdict


def main() -> int:
    farm = parse_input()
    region_index = build_index(farm)
    sum_ = 0

    for region_id in region_index:
        locs = region_index[region_id]
        sum_ += calculate_perimeter(locs) * len(locs)

    return sum_


def parse_input(input_file_path: str = "input.txt") -> list[list[str]]:
    farm = []

    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()
            farm.append(list(line))

    return farm


def build_index(farm: list[list[str]]) -> dict:
    last_used_id = 0
    index = defaultdict(set)  # region_id to list of locations map
    reverse_index = {}  # location to region_id map

    for i in range(len(farm)):
        for j in range(len(farm[0])):
            left_i, left_j = (i, j - 1)
            up_i, up_j = (i - 1, j)
            left_is_equal = left_j >= 0 and farm[i][j] == farm[left_i][left_j]
            up_is_equal = up_i >= 0 and farm[i][j] == farm[up_i][up_j]

            if left_is_equal and up_is_equal:
                up_region_id = reverse_index[(up_i, up_j)]
                left_region_id = reverse_index[(left_i, left_j)]

                if up_region_id != left_region_id:
                    index[left_region_id] |= index[up_region_id]

                    for loc in index[up_region_id]:
                        reverse_index[loc] = left_region_id

                    del index[up_region_id]

                region_id = left_region_id
            elif left_is_equal:
                region_id = reverse_index[(left_i, left_j)]
            elif up_is_equal:
                region_id = reverse_index[(up_i, up_j)]
            else:
                last_used_id += 1
                region_id = last_used_id

            index[region_id].add((i, j))
            reverse_index[(i, j)] = region_id

    return index


def calculate_perimeter(locations: set[tuple]) -> int:
    perimeter = 0

    for loc in locations:
        x, y = loc
        contrib = 4
        up = (x - 1, y)
        down = (x + 1, y)
        right = (x, y + 1)
        left = (x, y - 1)

        for direction in [up, down, left, right]:
            if direction in locations:
                contrib -= 1

        perimeter += contrib

    return perimeter


if __name__ == "__main__":
    print(main())

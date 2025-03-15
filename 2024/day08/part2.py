import itertools
from collections import defaultdict


def count_antinodes(antennas: dict) -> int:
    freq_index = build_frequency_index(antennas["frequencies"])
    antinodes = set()

    for symbol, locs in freq_index.items():
        pairs = itertools.combinations(locs, 2)

        for antenna1, antenna2 in pairs:
            diffx = antenna1[0] - antenna2[0]
            diffy = antenna1[1] - antenna2[1]

            multiplier = 0

            while within_boundary(
                (
                    antinode_up := (
                        antenna1[0] + diffx * multiplier,
                        antenna1[1] + diffy * multiplier,
                    )
                ),
                antennas,
            ):
                antinodes.add(antinode_up)
                multiplier += 1

            multiplier = 0

            while within_boundary(
                (
                    antinode_down := (
                        antenna2[0] - diffx * multiplier,
                        antenna2[1] - diffy * multiplier,
                    )
                ),
                antennas,
            ):
                antinodes.add(antinode_down)
                multiplier += 1

    return len(antinodes)


def build_frequency_index(frequencies: dict) -> dict:
    index = defaultdict(list)

    for freq in frequencies:
        symbol = freq["symbol"]
        loc = freq["loc"]
        index[symbol].append(loc)

    return index


def within_boundary(antinode: tuple[int], antennas: dict) -> bool:
    x, y = antinode
    max_x, max_y = antennas["size"]
    x_is_valid = 0 <= x < max_x
    y_is_valid = 0 <= y < max_y

    return x_is_valid and y_is_valid


def parse_input():
    with open("input.txt", "r") as f:
        row = 0
        frequencies = []

        for line in f:
            line = line.strip()

            for column, char in enumerate(line):
                if char == ".":
                    continue

                frequency = {"symbol": char, "loc": (row, column)}
                frequencies.append(frequency)

            row += 1

    return {"size": (row, column + 1), "frequencies": frequencies}


def main():
    antennas = parse_input()
    return count_antinodes(antennas)


if __name__ == "__main__":
    print(main())

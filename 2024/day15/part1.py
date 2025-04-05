def main():
    data = parse_input()
    warehouse_map = data["map"]
    moves = data["moves"]

    for direction in moves:
        move(warehouse_map, direction)

    sum_ = 0

    for i, _ in enumerate(warehouse_map["cells"]):
        for j, _ in enumerate(warehouse_map["cells"][i]):
            if warehouse_map["cells"][i][j] == "O":
                gps = 100 * i + j
                sum_ += gps

    return sum_


def move(warehouse_map: dict, direction: str) -> None:
    cells = warehouse_map["cells"]
    width, height = len(cells[0]), len(cells)
    curr_loc = warehouse_map["robot"]
    x, y = curr_loc

    match direction:
        case "^":
            next_loc = (x - 1, y)
        case ">":
            next_loc = (x, y + 1)
        case "v":
            next_loc = (x + 1, y)
        case "<":
            next_loc = (x, y - 1)

    next_char = cells[next_loc[0]][next_loc[1]]

    match next_char:
        case "#":
            next_loc = curr_loc
        case "O":
            match direction:
                case "^":
                    direction_iter = ((i, y) for i in range(x - 1, -1, -1))
                case ">":
                    direction_iter = ((x, i) for i in range(y + 1, width))
                case "v":
                    direction_iter = ((i, y) for i in range(x + 1, height))
                case "<":
                    direction_iter = ((x, i) for i in range(y - 1, -1, -1))

            empty_space_found = False

            for new_loc in direction_iter:
                if cells[new_loc[0]][new_loc[1]] == ".":
                    empty_space_found = True
                    break
                elif cells[new_loc[0]][new_loc[1]] == "#":
                    break

            if empty_space_found:
                cells[new_loc[0]][new_loc[1]] = "O"
                cells[next_loc[0]][next_loc[1]] = "@"
                cells[x][y] = "."
                warehouse_map["robot"] = next_loc
        case ".":
            cells[next_loc[0]][next_loc[1]] = "@"
            cells[x][y] = "."
            warehouse_map["robot"] = next_loc


def parse_input(input_file_path: str = "input.txt") -> dict:
    warehouse_map = {"robot": None, "cells": []}
    moves = []
    parse_state = "map"

    with open(input_file_path, "r") as f:
        line_no = 0

        for line in f:
            line = line.strip()

            if line == "":
                parse_state = "moves"
                continue

            match parse_state:
                case "map":
                    map_row = []

                    for i, c in enumerate(line):
                        map_row.append(c)

                        if c == "@":
                            warehouse_map["robot"] = (line_no, i)

                    warehouse_map["cells"].append(map_row)
                case "moves":
                    moves.extend([c for c in line])

            line_no += 1

    return {"map": warehouse_map, "moves": moves}


if __name__ == "__main__":
    print(main())

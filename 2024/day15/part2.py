def main():
    data = parse_input()
    warehouse_map = data["map"]
    moves = data["moves"]

    for direction in moves:
        move(warehouse_map, direction)

    sum_ = 0

    for i, _ in enumerate(warehouse_map["cells"]):
        for j, _ in enumerate(warehouse_map["cells"][i]):
            if warehouse_map["cells"][i][j] == "[":
                gps = 100 * i + j
                sum_ += gps

    return sum_


def print_cells(cells: list[list[int]]) -> None:
    for row in cells:
        for c in row:
            print(c, end="")
        print()


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
                        match c:
                            case "#" | ".":
                                map_row.extend([c] * 2)
                            case "O":
                                map_row.extend(["[", "]"])
                            case "@":
                                map_row.extend(["@", "."])
                                warehouse_map["robot"] = (line_no, i * 2)

                    warehouse_map["cells"].append(map_row)
                case "moves":
                    moves.extend([c for c in line])

            line_no += 1

    return {"map": warehouse_map, "moves": moves}


def move(warehouse_map: dict, direction: str) -> None:
    cells = warehouse_map["cells"]
    width, height = len(cells[0]), len(cells)
    curr_loc = warehouse_map["robot"]
    x, y = curr_loc
    next_loc = get_next_loc(curr_loc, direction)
    next_char = cells[next_loc[0]][next_loc[1]]
    cells_to_move = []
    traverse_state = {}
    traverse(cells, curr_loc, direction, cells_to_move, traverse_state)
    traverse_state.clear()

    match direction:
        case "^" | "<":
            cells_to_move.sort(key=lambda t: (t[0], t[1]))
        case "v" | ">":
            cells_to_move.sort(key=lambda t: (-t[0], -t[1]))

    for cell in cells_to_move:
        move_cell(cells, cell, direction)

    if cells_to_move or next_char == ".":
        robot = move_cell(cells, warehouse_map["robot"], direction)
        warehouse_map["robot"] = robot


def traverse(
    cells: list[list[int]],
    loc: tuple[int],
    direction: str,
    cells_to_move: list = [],
    traverse_state={},
) -> None:
    next_loc = get_next_loc(loc, direction)
    next_char = cells[next_loc[0]][next_loc[1]]

    if next_loc in cells_to_move:
        return

    if traverse_state.get("stop"):
        return

    match next_char:
        case "#":
            cells_to_move.clear()
            traverse_state["stop"] = True
            return
        case ".":
            return
        case "[" | "]":
            cells_to_move.append(next_loc)

            match direction:
                case ">" | "<":
                    closing_bracket_loc = get_next_loc(next_loc, direction)
                case "^" | "v":
                    if next_char == "[":
                        closing_bracket_loc = get_next_loc(next_loc, ">")
                    else:
                        closing_bracket_loc = get_next_loc(next_loc, "<")

            cells_to_move.append(closing_bracket_loc)
            traverse(cells, next_loc, direction, cells_to_move, traverse_state)
            traverse(
                cells, closing_bracket_loc, direction, cells_to_move, traverse_state
            )


def move_cell(cells: list[list[int]], loc: tuple[int], direction: str) -> tuple[int]:
    next_loc = get_next_loc(loc, direction)
    x, y = loc
    x_next, y_next = next_loc
    cells[x][y], cells[x_next][y_next] = cells[x_next][y_next], cells[x][y]
    return next_loc


def get_next_loc(curr_loc: tuple[int], direction: str) -> tuple[int]:
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

    return next_loc


if __name__ == "__main__":
    print(main())

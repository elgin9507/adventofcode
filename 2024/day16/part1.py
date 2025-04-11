import sys

sys.setrecursionlimit(15000)


def main():
    map_data = parse_input()
    scores = []
    traverse(
        map_data["cells"], map_data["start"], None, 0, {map_data["start"]: 0}, scores
    )

    return min(scores)


def parse_input(input_file_path="input.txt") -> dict:
    cells = []
    data = {"cells": cells}

    with open(input_file_path, "r") as f:
        i = 0

        for line in f:
            line = line.strip()
            row = []
            j = 0

            for char in line:
                match char:
                    case "S":
                        data["start"] = (i, j)
                    case "E":
                        data["end"] = (i, j)

                row.append(char)
                j += 1

            cells.append(row)
            i += 1

    return data


def print_cells(cells: list[list[int]]) -> None:
    for row in cells:
        for char in row:
            print(char, end="")
        print()


def traverse(
    cells: list[list[int]],
    loc: tuple[int],
    prev_loc: tuple[int] | None,
    curr_score: int,
    visited: set[tuple[int]],
    scores: list[int],
) -> list[int]:
    for direction in ("^", ">", "v", "<"):
        next_loc = get_next_loc(loc, direction)
        next_char = cells[next_loc[0]][next_loc[1]]
        step_score = calc_score(prev_loc, loc, next_loc)

        if next_loc in visited and visited[next_loc] < (curr_score + step_score):
            continue

        match next_char:
            case ".":
                visited[next_loc] = curr_score + step_score
                traverse(cells, next_loc, loc, curr_score + step_score, visited, scores)
            case "#":
                continue
            case "E":
                scores.append(curr_score + step_score)

    return scores


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


def calc_score(
    prev_loc: tuple[int] | None, curr_loc: tuple[int], next_loc: tuple[int]
) -> int:
    score = 1

    if prev_loc is not None:
        if prev_loc[0] == curr_loc[0]:
            if curr_loc[0] != next_loc[0]:
                score += 1000
        else:  # prev_loc[1] == curr_loc[1]:
            if curr_loc[1] != next_loc[1]:
                score += 1000

    return score


if __name__ == "__main__":
    print(main())

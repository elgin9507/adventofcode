from collections import defaultdict


def count_guard_positions(map_data: dict) -> int:
    def guard_turn_right(guard_data: dict) -> None:
        directions = "^>v<"
        old_direction = guard_data["direction"]
        new_direction_idx = directions.index(old_direction) + 1

        if new_direction_idx == len(directions):
            new_direction_idx = 0

        guard_data["direction"] = directions[new_direction_idx]

    def guard_move(map_data: dict, row_index: dict, col_index: dict) -> set[tuple]:
        current_position = map_data["guard"]["loc"]
        direction = map_data["guard"]["direction"]
        row, col = current_position
        visited_positions = set()

        if current_position == (-1, -1):
            breakpoint()

        match direction:
            case "^":
                obstructions = col_index[col]
                stop = -1

                for obst in obstructions[::-1]:
                    if obst < row:
                        stop = obst
                        break

                new_position = (stop + 1, col)

                while row > new_position[0]:
                    row -= 1
                    visited_positions.add((row, col, direction))
            case "v":
                obstructions = col_index[col]
                stop = map_data["size"][0]

                for obst in obstructions:
                    if obst > row:
                        stop = obst
                        break

                new_row = stop - 1
                new_position = (new_row, col)

                while new_row > row:
                    visited_positions.add((new_row, col, direction))
                    new_row -= 1
            case "<":
                obstructions = row_index[row]
                stop = -1

                for obst in obstructions[::-1]:
                    if obst < col:
                        stop = obst
                        break

                new_position = (row, stop + 1)

                while col > new_position[1]:
                    col -= 1
                    visited_positions.add((row, col, direction))
            case ">":
                obstructions = row_index[row]
                stop = map_data["size"][1]

                for obst in obstructions:
                    if obst > col:
                        stop = obst
                        break

                new_col = stop - 1
                new_position = (row, new_col)

                while new_col > col:
                    visited_positions.add((row, new_col, direction))
                    new_col -= 1

        map_data["guard"]["loc"] = new_position
        guard_turn_right(map_data["guard"])

        return visited_positions

    def guard_patrol(map_data: dict, row_index: dict, col_index: dict) -> int:
        visited_positions = {map_data["guard"]["loc"]}
        max_row, max_col = map_data["size"]
        new_obstructions = set()

        while True:
            old_direction = map_data["guard"]["direction"]
            new_positions = guard_move(map_data, row_index, col_index)

            for x, y, _ in new_positions:
                match old_direction:
                    case "<":
                        diff = 1

                        while diff < x:
                            if (x - diff, y, "^") in visited_positions or (x - diff, y, "v") in visited_positions:
                                new_obstructions.add((x, y - 1))
                                break

                            diff += 1
                    case ">":
                        diff = 1

                        while x + diff < max_row:
                            if (x + diff, y, "v") in visited_positions or (x + diff, y, "^") in visited_positions:
                                new_obstructions.add((x, y + 1))
                                break

                            diff += 1
                    case "^":
                        diff = 1

                        while y + diff < max_col:
                            if (x, y + diff, ">") in visited_positions or (x, y + diff, "<") in visited_positions:
                                new_obstructions.add((x - 1, y))
                                break

                            diff += 1
                    case "v":
                        diff = 1

                        while diff < y:
                            if (x, y - diff, "<") in visited_positions or (x, y - diff, ">") in visited_positions:
                                new_obstructions.add((x + 1, y))
                                break

                            diff += 1


            visited_positions |= new_positions
            row, col = map_data["guard"]["loc"]

            if row == max_row - 1 or col == max_col - 1 or row == 0 or col == 0:
                break

        return new_obstructions

    def index_map_data(map_data: dict) -> list[dict]:
        row_index = defaultdict(list)
        col_index = defaultdict(list)

        for x, y in map_data["obstructions"]:
            row_index[x].append(y)
            col_index[y].append(x)

        return [row_index, col_index]

    row_index, col_index = index_map_data(map_data)
    new_obstructions = guard_patrol(map_data, row_index, col_index)
    # ((6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7))
    print(new_obstructions)
    return len(new_obstructions)


if __name__ == "__main__":
    map_data = {"size": None, "obstructions": [], "guard": {}}
    row_counter = 0

    with open("input.txt", "r") as f:
        for line in f:
            col_counter = 0

            for c in line.strip():
                match c:
                    case "#":
                        map_data["obstructions"].append((row_counter, col_counter))
                    case "^" | ">" | "v" | "<":
                        map_data["guard"] = {
                            "loc": (row_counter, col_counter),
                            "direction": c,
                        }
                    case _:
                        pass

                col_counter += 1

            row_counter += 1

        map_data["size"] = (row_counter, col_counter)

    print(count_guard_positions(map_data))

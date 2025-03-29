import math

MOVES = 100
TILES = (101, 103)


def main() -> int:
    robots = parse_input()

    for robot in robots:
        move(robot, TILES, MOVES)

    quarter_counts = count(robots, TILES)
    safety_index = math.prod(quarter_counts)

    return safety_index


def parse_input(input_file_path: str = "input.txt") -> list[dict]:
    robots = []

    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()
            robot_data, velocity_data = line.split(" ", 1)
            robot_x, robot_y = robot_data.split("=")[1].split(",")
            velocity_x, velocity_y = velocity_data.split("=")[1].split(",")
            robot = {
                "x": int(robot_x),
                "y": int(robot_y),
                "velocity": (int(velocity_x), int(velocity_y)),
            }
            robots.append(robot)

    return robots


def move(robot: dict, tiles: tuple[int], times: int) -> None:
    x, y = robot["x"], robot["y"]
    velocity_x, velocity_y = robot["velocity"]
    x += velocity_x * times
    y += velocity_y * times
    width, height = tiles

    if x < 0:
        x += math.ceil(abs(x) / width) * width
    elif x >= width:
        x -= math.floor(x / width) * width

    if y < 0:
        y += math.ceil(abs(y) / height) * height
    elif y >= height:
        y -= math.floor(y / height) * height

    robot["x"], robot["y"] = x, y


def count(robots: list[dict], tiles: tuple[int]) -> tuple[int]:
    quarter1 = quarter2 = quarter3 = quarter4 = 0
    mid_x, mid_y = tiles[0] // 2, tiles[1] // 2

    for robot in robots:
        x, y = robot["x"], robot["y"]

        if x < mid_x:
            if y < mid_y:
                quarter1 += 1
            elif y > mid_y:
                quarter3 += 1
        elif x > mid_x:
            if y < mid_y:
                quarter2 += 1
            elif y > mid_y:
                quarter4 += 1

    return (quarter1, quarter2, quarter3, quarter4)


if __name__ == "__main__":
    print(main())

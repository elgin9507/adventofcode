def parse_input(input_data_path: str) -> list[dict]:
    calibrations = []

    with open(input_data_path, "r") as f:
        for line in f:
            line = line.strip()
            target, numbers = line.split(":")

            calibration = {
                "target": int(target),
                "numbers": [int(n) for n in numbers.strip().split(" ")],
            }
            calibrations.append(calibration)

    return calibrations


def total_result(calibrations: list[dict]) -> int:
    total_sum = 0

    for cal in calibrations:
        target, numbers = cal["target"], cal["numbers"]
        if is_valid(target, numbers):
            total_sum += target

    return total_sum


def is_valid(target: int, numbers: list[int]) -> bool:
    if len(numbers) == 2:
        a, b = numbers
        return a + b == target or a * b == target or concat(a, b) == target

    a, b = numbers[0], numbers[1]
    sum_ = a + b
    mul_ = a * b
    con_ = concat(a, b)

    return (
        is_valid(target, [sum_, *numbers[2:]])
        or is_valid(target, [mul_, *numbers[2:]])
        or is_valid(target, [con_, *numbers[2:]])
    )


def concat(num1: int, num2: int) -> int:
    return int(f"{num1}{num2}")


if __name__ == "__main__":
    calibrations = parse_input("input.txt")
    print(total_result(calibrations))

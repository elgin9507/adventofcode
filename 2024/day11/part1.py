def main() -> int:
    numbers = parse_input()

    for i in range(25):
        transform_list(numbers)

    return len(numbers)


def parse_input(input_file_path: str = "input.txt") -> list[int]:
    with open(input_file_path, "r") as f:
        first_line = f.readline().strip()

    return [int(x) for x in first_line.split(" ")]


def transform_list(numbers: list[int]) -> list[int]:
    i = 0

    while i < len(numbers):
        transformed = transform_number(numbers[i])

        match transformed:
            case int():
                numbers[i] = transformed
                i += 1
            case tuple():
                numbers[i : i + 1] = transformed
                i += 2
            case _:
                raise ValueError

    return numbers


def transform_number(number: int) -> int | tuple:
    match number:
        case 0:
            result = 1
        case _ if len(str(number)) % 2 == 0:
            left = int(str(number)[: len(str(number)) // 2])
            right = int(str(number)[len(str(number)) // 2 :])
            result = (left, right)
        case _:
            result = number * 2024

    return result


if __name__ == "__main__":
    print(main())

from functools import lru_cache


def main() -> int:
    numbers = parse_input()
    n = 75
    sum_ = 0

    for num in numbers:
        sum_ += transformn(num, n)

    return sum_


def parse_input(input_file_path: str = "input.txt") -> list[int]:
    with open(input_file_path, "r") as f:
        first_line = f.readline().strip()

    return [int(x) for x in first_line.split(" ")]


@lru_cache(maxsize=None)
def transformn(number: int, n: int) -> int:
    if n == 0:
        return 1

    transformed = transform(number)

    if isinstance(transformed, tuple):
        left, right = transformed
        return transformn(left, n - 1) + transformn(right, n - 1)
    else:
        return transformn(transformed, n - 1)


def transform(number: int) -> int | tuple:
    str_num = str(number)
    num_len = len(str_num)

    if number == 0:
        transformed = 1
    elif num_len % 2 == 0:
        left = int(str_num[: num_len // 2])
        right = int(str_num[num_len // 2 :])
        transformed = (left, right)
    else:
        transformed = number * 2024

    return transformed


if __name__ == "__main__":
    print(main())

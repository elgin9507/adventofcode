def calculate(input_str):
    ops = []
    valid_sequence = ["m", "u", "l", "(", "d1", ",", "d2", ")"]
    last_parsed = -1
    parsed_nums = ["", ""]

    for c in input_str:
        if last_parsed == len(valid_sequence) - 1:
            ops.append(int(parsed_nums[0]) * int(parsed_nums[1]))
            parsed_nums = ["", ""]
            last_parsed = -1

        expected = valid_sequence[last_parsed + 1]

        if expected == "d1":
            if c.isnumeric():
                parsed_nums[0] += c
            elif c == ",":
                last_parsed += 2
            else:
                parsed_nums = ["", ""]
                last_parsed = -1
        elif expected == "d2":
            if c.isnumeric():
                parsed_nums[1] += c
            elif c == ")":
                last_parsed += 2
            else:
                parsed_nums = ["", ""]
                last_parsed = -1
        else:
            if expected == c:
                last_parsed += 1
            else:
                parsed_nums = ["", ""]
                last_parsed = -1

    return sum(ops)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_str = f.read()
    print(calculate(input_str))

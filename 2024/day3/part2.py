def calculate(input_str):
    ops = []
    valid_sequence = ["m", "u", "l", "(", "d1", ",", "d2", ")"]
    enable_sequence = ["d", "o", "(", ")"]
    disable_sequence = ["d", "o", "n", "'", "t", "(", ")"]
    op_enabled = True

    def parse_mul(c, state):
        nonlocal ops

        if state["last_parsed"] == len(valid_sequence) - 1:
            ops.append(int(state["parsed_nums"][0]) * int(state["parsed_nums"][1]))
            state["parsed_nums"] = ["", ""]
            state["last_parsed"] = -1

        expected = valid_sequence[state["last_parsed"] + 1]

        if expected == "d1":
            if c.isnumeric():
                state["parsed_nums"][0] += c
            elif c == ",":
                state["last_parsed"] += 2
            else:
                state["parsed_nums"] = ["", ""]
                state["last_parsed"] = -1
        elif expected == "d2":
            if c.isnumeric():
                state["parsed_nums"][1] += c
            elif c == ")":
                state["last_parsed"] += 2
            else:
                state["parsed_nums"] = ["", ""]
                state["last_parsed"] = -1
        else:
            if expected == c:
                state["last_parsed"] += 1
            else:
                state["parsed_nums"] = ["", ""]
                state["last_parsed"] = -1

    def parse_enable(c, state):
        nonlocal op_enabled

        if state["last_parsed"] == len(enable_sequence) - 1:
            op_enabled = True
            state["last_parsed"] = -1

        expected = enable_sequence[state["last_parsed"] + 1]

        if expected == c:
            state["last_parsed"] += 1
        else:
            state["last_parsed"] = -1

    def parse_disable(c, state):
        nonlocal op_enabled

        if state["last_parsed"] == len(disable_sequence) - 1:
            op_enabled = False
            state["last_parsed"] = -1

        expected = disable_sequence[state["last_parsed"] + 1]

        if expected == c:
            state["last_parsed"] += 1
        else:
            state["last_parsed"] = -1

    parse_mul_state = {"last_parsed": -1, "parsed_nums": ["", ""]}
    enable_state = {"last_parsed": -1}
    disable_state = {"last_parsed": -1}

    for c in input_str:
        parse_enable(c, enable_state)
        parse_disable(c, disable_state)

        if op_enabled:
            parse_mul(c, parse_mul_state)
        else:
            parse_mul_state = {"last_parsed": -1, "parsed_nums": ["", ""]}

    return sum(ops)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_str = f.read()
    print(calculate(input_str))

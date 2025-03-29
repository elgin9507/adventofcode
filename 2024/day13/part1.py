COST_A = 3
COST_B = 1


def main() -> int:
    machines = parse_input()
    sum_ = 0

    for machine in machines:
        cheapest = solve_machine(machine)

        if cheapest is not None:
            sum_ += cheapest

    return sum_


def solve_machine(machine: dict) -> int | None:
    costs = {(0, 0): 0}
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop(0)
        current_cost = costs[(x, y)]

        new_x, new_y = x + machine["A"][0], y + machine["A"][1]

        if new_x <= machine["Prize"][0] and new_y <= machine["Prize"][1]:
            if (new_x, new_y) not in costs or costs[
                (new_x, new_y)
            ] > current_cost + COST_A:
                costs[(new_x, new_y)] = current_cost + COST_A
                queue.append((new_x, new_y))

        new_x, new_y = x + machine["B"][0], y + machine["B"][1]

        if new_x < machine["Prize"][0] and new_y <= machine["Prize"][1]:
            if (new_x, new_y) not in costs or costs[
                (new_x, new_y)
            ] > current_cost + COST_B:
                costs[(new_x, new_y)] = current_cost + COST_B
                queue.append((new_x, new_y))

    return costs.get((machine["Prize"][0], machine["Prize"][1]), None)


def parse_input(input_file_path: str = "input.txt") -> list[dict]:
    claw_machines = []

    with open(input_file_path, "r") as f:
        machine = {}

        for line in f:
            line = line.strip()

            if not line:
                continue

            if not machine:
                expected = "Button A:"
                sep = "+"
                key = "A"
                end = False
            elif "A" in machine and "B" not in machine:
                expected = "Button B:"
                sep = "+"
                key = "B"
                end = False
            else:
                expected = "Prize:"
                sep = "="
                key = "Prize"
                end = True

            line = line.strip(expected).strip()
            x_data, y_data = line.split(", ")
            x = int(x_data.split(sep)[1])
            y = int(y_data.split(sep)[1])
            machine[key] = (x, y)

            if end:
                claw_machines.append(machine.copy())
                machine.clear()

    return claw_machines


if __name__ == "__main__":
    print(main())

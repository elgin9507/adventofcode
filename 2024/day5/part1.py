from collections import defaultdict


def sum_updates(rules: list[tuple], updates: list[tuple]) -> int:
    def is_valid(update: tuple) -> bool:
        for i in range(len(update) - 1):
            curr = update[i]
            next_ = update[i + 1]

            if next_ not in before_map[curr]:
                return False

        return True

    def middle(update: tuple) -> int:
        return update[len(update) // 2]

    before_map = defaultdict(set)

    for left, right in rules:
        before_map[left].add(right)

    sum_ = sum([middle(update) for update in updates if is_valid(update)])

    return sum_


if __name__ == "__main__":
    rules = []
    updates = []

    with open("input.txt", "r") as f:
        for line in f:
            if not line.strip():
                break

            rules.append(tuple([int(x) for x in line.strip().split("|")]))

        for line in f:
            updates.append(tuple([int(x) for x in line.strip().split(",")]))

    print(sum_updates(rules, updates))

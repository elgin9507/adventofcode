from collections import defaultdict


def sum_updates(rules: list[tuple], updates: list[list]) -> int:
    def is_valid(update: list) -> bool:
        for i in range(len(update) - 1):
            curr = update[i]
            next_ = update[i + 1]

            if next_ not in before_map[curr]:
                return False

        return True

    def reorder(update: list) -> None:
        n = len(update)

        for i in range(n - 2, -1, -1):
            j = i + 1

            while j < n and update[j] not in before_map[update[j - 1]]:
                update[j], update[j - 1] = update[j - 1], update[j]
                j += 1

    def middle(update: list) -> int:
        return update[len(update) // 2]

    before_map = defaultdict(set)

    for left, right in rules:
        before_map[left].add(right)

    sum_ = 0

    for update in updates:
        if not is_valid(update):
            reorder(update)
            sum_ += middle(update)

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
            updates.append([int(x) for x in line.strip().split(",")])

    print(sum_updates(rules, updates))

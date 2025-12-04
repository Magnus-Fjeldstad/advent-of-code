def parse_input(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


lines = parse_input("./2025/day3/input.txt")


def hj(bank):
    k = 12
    to_romove = len(bank) - k
    stack = []

    for cell in bank:
        while to_romove > 0 and stack and stack[-1] < cell:
            stack.pop()
            to_romove -= 1
        stack.append(cell)

    return "".join(stack[:k])


def solve(path):
    lines = parse_input(path)
    total = 0
    for bank in lines:
        best = int(hj(bank))
        total += best
    return total


print(solve("./2025/day3/test.txt"))

def parse_input(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


lines = parse_input("./2025/day4/input.txt")


def check_adjacent(pallet):
    h = len(pallet)
    w = len(pallet[0])
    total_sum = 0

    for i in range(h):
        for j in range(w):
            neighbors = []

            if pallet[i][j] != "@":
                continue

            # Right
            if j + 1 < w and pallet[i][j + 1]:
                neighbors.append(pallet[i][j + 1])

            # Left
            if j - 1 >= 0 and pallet[i][j - 1]:
                neighbors.append(pallet[i][j - 1])

            # Up
            if i - 1 >= 0 and pallet[i - 1][j]:
                neighbors.append(pallet[i - 1][j])

            # Down
            if i + 1 < h and pallet[i + 1][j]:
                neighbors.append(pallet[i + 1][j])

            # Left Up
            if i - 1 >= 0 and j - 1 >= 0 and pallet[i - 1][j - 1]:
                neighbors.append(pallet[i - 1][j - 1])

            # Left Down
            if i + 1 < h and j - 1 >= 0 and pallet[i + 1][j - 1]:
                neighbors.append(pallet[i + 1][j - 1])

            # Right Up
            if i - 1 >= 0 and j + 1 < w and pallet[i - 1][j + 1]:
                neighbors.append(pallet[i - 1][j + 1])

            # Right Down
            if i + 1 < h and j + 1 < w and pallet[i + 1][j + 1]:
                neighbors.append(pallet[i + 1][j + 1])

            if neighbors.count("@") < 4:
                total_sum += 1

    return total_sum


def check_adjacent_new(pallet):
    pallet = [list(row) for row in pallet]
    h = len(pallet)
    w = len(pallet[0])
    total_sum = 0

    while True:
        remove_list = []

        for i in range(h):
            for j in range(w):
                if pallet[i][j] != "@":
                    continue

                neighbors = []

                # Right
                if j + 1 < w and pallet[i][j + 1]:
                    neighbors.append(pallet[i][j + 1])
                # Left
                if j - 1 >= 0 and pallet[i][j - 1]:
                    neighbors.append(pallet[i][j - 1])
                # Up
                if i - 1 >= 0 and pallet[i - 1][j]:
                    neighbors.append(pallet[i - 1][j])
                # Down
                if i + 1 < h and pallet[i + 1][j]:
                    neighbors.append(pallet[i + 1][j])
                # Left Up
                if i - 1 >= 0 and j - 1 >= 0 and pallet[i - 1][j - 1]:
                    neighbors.append(pallet[i - 1][j - 1])
                # Left Down
                if i + 1 < h and j - 1 >= 0 and pallet[i + 1][j - 1]:
                    neighbors.append(pallet[i + 1][j - 1])
                # Right Up
                if i - 1 >= 0 and j + 1 < w and pallet[i - 1][j + 1]:
                    neighbors.append(pallet[i - 1][j + 1])
                # Right Down
                if i + 1 < h and j + 1 < w and pallet[i + 1][j + 1]:
                    neighbors.append(pallet[i + 1][j + 1])

                if neighbors.count("@") < 4:
                    remove_list.append((i, j))

        if not remove_list:
            return total_sum

        for x, y in remove_list:
            pallet[x][y] = "."
            total_sum += 1


print(check_adjacent(lines))
print(check_adjacent_new(lines))

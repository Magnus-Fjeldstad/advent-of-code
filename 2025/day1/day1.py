def parse_input(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


lines = parse_input("./2025/input.txt")


def get_num(rotation):
    return int(rotation[1:])


def crack_password(lines):
    count0 = 0
    current = 50
    for rot in lines:
        n = get_num(rot)
        if rot.startswith("R"):
            current = (current + n) % 100
        else:
            current = (current - n) % 100
        if current == 0:
            count0 += 1
    return count0


def new_password_method(lines):
    count = 0
    current = 50
    for rot in lines:
        n = get_num(rot)
        if rot.startswith("R"):
            for i in range(1, n + 1):
                current = (current + 1) % 100
                if current == 0:
                    count += 1
        else:
            for i in range(1, n + 1):
                current = (current - 1) % 100
                if current == 0:
                    count += 1
    return count


print(crack_password(lines))
print(new_password_method(lines))

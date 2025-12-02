def parse_input(path):
    with open(path, "r", encoding="utf-8") as f:
        line = f.read().strip()
        parts = line.split(",")
        return [(int(a), int(b)) for a, b in (p.split("-") for p in parts)]


id_range = parse_input("./2025/day2/input_day_2.txt")


def get_range(id_ranges):

    result = []

    for start, end in id_ranges:
        current = list(range(start, end + 1))
        result.append(current)

    return result


all_num_range = get_range(id_range)


def get_invalid_ids(range):
    invlidIdStr = 0

    for nums in range:
        for num in nums:
            strNum = str(num)
            mid = len(strNum) // 2
            if len(strNum) % 2 == 0:
                first = strNum[:mid]
                second = strNum[mid:]
                if first == second:
                    invlidIdStr += num

    return invlidIdStr


def is_repeated_pattern(s):
    n = len(s)
    for k in range(1, n // 2 + 1):

        if n % k != 0:
            continue
        pattern = s[:k]
        if pattern * (n // k) == s:
            return True
    return False


def get_invalid_sum(ranges):
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            strNum = str(num)
            if is_repeated_pattern(strNum):
                total += num
    return total


answer = get_invalid_sum(id_range)
print(answer)

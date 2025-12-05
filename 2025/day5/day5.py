def parse_input(path):
    ranges = []
    numbers = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "-" in line:
                start, end = line.split("-")
                ranges.append((int(start), int(end)))
            else:
                numbers.append(int(line))
    return ranges, numbers


fresh_range, ingredients = parse_input("./2025/day5/input.txt")


def check_fresh(fresh_range, ingredients):
    num_fresh = 0

    for num in ingredients:
        for start, end in fresh_range:
            min_val = start
            max_val = end
            if min_val <= num <= max_val:
                num_fresh += 1
                break

    return num_fresh


def all_fresh_ranges(fresh_range):

    fresh_range_sorted = sorted(fresh_range)

    merged = []
    current_start, current_end = fresh_range_sorted[0]

    for start, end in fresh_range_sorted[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    total = 0

    for start, end in merged:
        total += end - start + 1

    return total


print(check_fresh(fresh_range, ingredients))
print(all_fresh_ranges(fresh_range))

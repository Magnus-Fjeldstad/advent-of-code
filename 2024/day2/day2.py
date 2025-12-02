def parse_input(path):
    report = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            numbers = [int(x) for x in line.strip().split()]
            report.append(numbers)
    return report


reports = parse_input("./2024/day2/test.txt")

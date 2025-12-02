# Read the location IDs from the file
left = []
right = []

with open("./2024/input2024.txt", "r") as f:
    for line in f:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

# Sort both lists
left_sorted = sorted(left)
right_sorted = sorted(right)

# Calculate the total distance
total_distance = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))

print(total_distance)

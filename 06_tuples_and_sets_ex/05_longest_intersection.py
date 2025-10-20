n = int(input())
longest_intersection = []

for _ in range(n):
    first_set = set()
    second_set = set()
    current_intersection = []

    first_range, second_range = input().split("-")

    first_start, first_end = first_range.split(",")
    first_start, first_end = int(first_start), int(first_end)

    second_start, second_end = second_range.split(",")
    second_start, second_end = int(second_start), int(second_end)

    for num in range(first_start, first_end + 1):
        first_set.add(num)

    for num in range(second_start, second_end + 1):
        second_set.add(num)

    current_intersection = list(first_set.intersection(second_set))
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

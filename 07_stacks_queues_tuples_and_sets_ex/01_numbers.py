first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "Check" and command[1] == "Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

    add_or_remove = command[0]
    first_or_second = command[1]
    numbers = command[2:]
    numbers = [int(x) for x in numbers]

    if add_or_remove == "Add" and first_or_second == "First":
        for num in numbers:
            first_sequence.add(num)

    if add_or_remove == "Add" and first_or_second == "Second":
        for num in numbers:
            second_sequence.add(num)

    if add_or_remove == "Remove" and first_or_second == "First":
        for num in numbers:
            if num in first_sequence:
                first_sequence.remove(num)

    if add_or_remove == "Remove" and first_or_second == "Second":
        for num in numbers:
            if num in second_sequence:
                second_sequence.remove(num)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

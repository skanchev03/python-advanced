numbers = tuple(input().split())
set_of_numbers = set()

for num in numbers:
    if num not in set_of_numbers:
        print(f"{float(num):.1f} - {numbers.count(num)} times")
    set_of_numbers.add(num)

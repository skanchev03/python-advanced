n = int(input())
odd = set()
even = set()

for row in range(1,n + 1):
    name = input()
    name_sum = 0

    for ch in name:
        name_sum += ord(ch)

    name_sum = name_sum // row

    if name_sum % 2 != 0:
        odd.add(name_sum)
    else:
        even.add(name_sum)

sum_odd = sum(odd)
sum_even = sum(even)

if sum_odd == sum_even:
    result = odd.union(even)
elif sum_odd > sum_even:
    result = odd.difference(even)
else:
    result = odd.symmetric_difference(even)

print(", ".join(str(x) for x in result))

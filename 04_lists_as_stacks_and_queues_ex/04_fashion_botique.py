clothes = [int(x) for x in input().split()]
capacity = int(input())
racks = 0

while clothes:
    racks += 1
    current_rack = 0
    while clothes and current_rack + clothes[-1] <= capacity:
        current_rack += clothes.pop()

print(racks)

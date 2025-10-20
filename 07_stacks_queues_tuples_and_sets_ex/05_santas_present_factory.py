from collections import deque


toy_magic = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

crafted_toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials and magic:
    current_material = materials[-1]
    current_magic = magic[0]

    if current_material == 0 and current_magic == 0:
        materials.pop()
        magic.popleft()
        continue

    elif current_material == 0:
        materials.pop()
        continue

    elif current_magic == 0:
        magic.popleft()
        continue

    total_magic = current_material * current_magic

    crafted = False
    for toy, value in toy_magic.items():
        if total_magic == value:
            crafted_toys[toy] += 1
            materials.pop()
            magic.popleft()
            crafted = True
            break

    if crafted:
        continue

    if total_magic < 0:
        materials.pop()
        magic.popleft()
        materials.append(current_magic + current_material)

    else:
        magic.popleft()
        materials[-1] += 15

success = (crafted_toys["Doll"] > 0 and crafted_toys["Wooden train"] > 0) or \
          (crafted_toys["Teddy bear"] > 0 and crafted_toys["Bicycle"] > 0)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy, count in sorted(crafted_toys.items()):
    if count > 0:
        print(f"{toy}: {count}")

text = list(input())
unique = set()

for el in text:
    unique.add(el)

unique = sorted(unique)

for el in unique:
    print(f"{el}: {text.count(el)} time/s")

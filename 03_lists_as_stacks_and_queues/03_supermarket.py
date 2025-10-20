from collections import deque


shoppers = deque()

while True:
    name = input()

    if name == "End":
        break

    if name == "Paid":
        while shoppers:
            print(shoppers.pop())
        continue

    shoppers.appendleft(name)

print(f"{len(shoppers)} people remaining.")

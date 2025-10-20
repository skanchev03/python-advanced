from collections import deque


water = int(input())
people = deque()

while True:
    name = input()

    if name == "Start":
        break

    people.append(name)

while True:
    command = input()

    if command == "End":
        break

    if command.isdigit():
        liters = int(command)
        if liters <= water:
            print(f"{people.popleft()} got water")
            water -= liters
        else:
            print(f"{people.popleft()} must wait")

    if command.startswith("refill"):
        command, liters = command.split()
        liters = int(liters)
        water += liters

print(f"{water} liters left")

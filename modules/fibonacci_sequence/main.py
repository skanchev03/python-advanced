from modules.fibonacci_sequence.core import create_sequence, locate


sequence = []

while True:
    line = input().split()
    command = line[0]

    if command == "Stop":
        break

    if command == "Create":
        count = int(line[2])
        sequence = create_sequence(count)
        print(" ".join(map(str, sequence)))

    elif command == "Locate":
        number = int(line[1])
        print(locate(number, sequence))

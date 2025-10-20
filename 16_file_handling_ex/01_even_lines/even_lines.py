SYMBOLS_TO_REPLACE = ("-", ",", ".", "!", "?")


with open("text.txt") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            for char in SYMBOLS_TO_REPLACE:
                line = line.replace(char, "@")
            line_list = line.split()
            print(" ".join(reversed(line_list)))

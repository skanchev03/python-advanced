import os


while True:
    line = input()

    if line == "End":
        break

    command, file_name, *args = line.split("-")

    if command == "Create":
        open(file_name, "w").close()

    elif command == "Add":
        content = args[0]

        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_string, new_string = args[0], args[1]

        try:
            with open(file_name, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

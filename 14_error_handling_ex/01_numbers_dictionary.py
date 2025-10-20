numbers_dictionary = {}

while True:
    number_as_string = input()

    if number_as_string == "Search":
        break

    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number

while True:
    searched = input()

    if searched == "Remove":
        break

    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

while True:
    searched = input()

    if searched == "End":
        break

    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)

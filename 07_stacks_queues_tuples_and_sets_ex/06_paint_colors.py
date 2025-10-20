from collections import deque


substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
color_requirements = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"}
    }

found_colors = []

while substrings:
    if len(substrings) > 1:
        first_substring = substrings.popleft()
        second_substring = substrings.pop()
    else:
        first_substring = substrings.popleft()
        second_substring = ""

    concatenated_first_to_second = first_substring + second_substring
    concatenated_second_to_first = second_substring + first_substring

    if concatenated_first_to_second in main_colors or concatenated_first_to_second in secondary_colors:
        found_colors.append(concatenated_first_to_second)
    elif concatenated_second_to_first in main_colors or concatenated_second_to_first in secondary_colors:
        found_colors.append(concatenated_second_to_first)
    else:
        first_substring = first_substring[:-1]
        second_substring = second_substring[:-1]

        middle_index = len(substrings) // 2

        if first_substring:
            substrings.insert(middle_index, first_substring)
            middle_index += 1

        if second_substring:
            substrings.insert(middle_index, second_substring)

final_colors = []
for color in found_colors:
    if color in secondary_colors:
        # Only keep if its required main colors were found
        if color_requirements[color].issubset(found_colors):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)

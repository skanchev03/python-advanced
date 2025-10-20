from string import punctuation


output = []

with open("text.txt") as text_file, open("output.txt", "w") as output_file:
    for index, line in enumerate(text_file):
        letters = 0
        punctuation_marks = 0

        for char in line:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                punctuation_marks += 1

        output.append(f"Line {index + 1}: {line.strip()} ({letters})({punctuation_marks})")

    output_file.write("\n".join(output))

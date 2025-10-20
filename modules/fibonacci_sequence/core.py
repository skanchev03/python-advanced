def create_sequence(count: int):
    sequence = [0, 1]

    for _ in range(count-2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def locate(number: int, sequence: list):
    try:
        return f"The number - {number} is at index {sequence.index(number)}"
    except ValueError:
        return f"The number {number} in not in the sequence"

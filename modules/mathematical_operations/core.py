def unpack_input(expression: list):
    number_one = float(expression[0])
    sign = expression[1]
    number_two = int(expression[2])
    return number_one, sign, number_two

mapper = {
    "/" : lambda a, b: a / b,
    "*": lambda a, b: a * b,
    "-": lambda a, b: a - b,
    "+": lambda a, b: a + b,
    "^": lambda a, b: a ** b,
}

def calculate(num_one: float, sign: str, num_two: int):
    return f"{mapper[sign](num_one, num_two):.2f}"

from collections import deque


expression_deque = deque(input().split())
result = deque()

operations = {
    "*": lambda x, y: x*y,
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "/": lambda x, y: x//y,
}

while expression_deque:
    operator = expression_deque.popleft()

    if operator in "*+-/":
        while len(result) != 1:
            first_num = result.popleft()
            second_num = result.popleft()
            result.appendleft(operations[operator](first_num, second_num))

    else:
        result.append(int(operator))

print(*result)

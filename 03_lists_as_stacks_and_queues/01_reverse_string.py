input_string = input()
stack = []
for i in input_string:
    stack.append(i)

for _ in range(len(stack)):
    last_el = stack.pop()
    print(last_el,end="")

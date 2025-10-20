parentheses_stack = list(input())
opening_parentheses_stack = []
balanced = True

for parentheses in parentheses_stack:
    if parentheses in "({[":
        opening_parentheses_stack.append(parentheses)
    elif parentheses in ")}]":
        if not opening_parentheses_stack:
            balanced = False
            break
        pair = opening_parentheses_stack.pop() + parentheses
        if pair not in ["()", "{}", "[]"]:
            balanced = False
            break

if opening_parentheses_stack:
    balanced = False

if balanced:
    print("YES")
else:
    print("NO")

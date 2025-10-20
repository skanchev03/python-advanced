stack = []
n = int(input())

mapper = {
    "1": lambda a: stack.append(int(a)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None,
}

for _ in range(n):
    query = input().split()
    mapper[query[0]](*query[1:])

if stack:
    print(", ".join(map(str, reversed(stack))))

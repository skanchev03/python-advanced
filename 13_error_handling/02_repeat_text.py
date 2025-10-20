text = input()
times = None

try:
    times = int(input())
except ValueError:
    print("Variable times must be an integer")

if times:
    print(text * times)

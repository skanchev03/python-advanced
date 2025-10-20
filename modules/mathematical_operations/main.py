from modules.mathematical_operations.core import calculate, unpack_input


expression = input().split()
print(calculate(*unpack_input(expression)))

import os.path
from constants import  path_to_dir

path = os.path.join(path_to_dir, "00_files", "numbers.txt")

file = open(path)
numbers = [int(num) for num in file.read().split("\n") if num]
print(sum(numbers))

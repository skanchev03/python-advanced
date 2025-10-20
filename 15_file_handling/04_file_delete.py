import os.path
from constants import  path_to_dir

path = os.path.join(path_to_dir, "15_file_handling", "my_first_file.txt")

try:
    os.remove(path)
except FileNotFoundError:
    print("File already deleted")

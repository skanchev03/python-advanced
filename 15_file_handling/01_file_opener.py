import os.path
from constants import  path_to_dir

path = os.path.join(path_to_dir, "00_files", "text.txt")

try:
    file = open(path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")

import re
from collections import defaultdict

with open("day7_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines()]

dir_structure = defaultdict(lambda: {"subdir": [], "size": 0})
ch_dir = False
search_dir = False
for line in inputs:
    if re.match(r"^\$\scd\s[^\.\s]*$", line):
        dir_name = re.match(r"\$\scd\s([^\.\s]*)", line).group(1)
        ch_dir = True
        search_dir = False
    elif ch_dir and line == "$ ls":
        search_dir = True
        ch_dir = False
    elif search_dir:
        if line[:3] == "dir":
            sub_dir_name = re.match(r"^dir\s(.*)$", line).group(1)
            dir_structure[dir_name]["subdir"].append(sub_dir_name)
        elif re.match(r"^(\d+)\s.*$", line):
            size = int(re.match(r"^(\d+)\s.*$", line).group(1))
            dir_structure[dir_name]["size"] += size
        else:
            search_dir = False
        ch_dir = False


def get_dir_size(dir_name: str) -> int:
    size = dir_structure[dir_name]["size"]
    print(dir_structure[dir_name]["subdir"])
    if not dir_structure[dir_name]["subdir"]:
        return size
    for sub_dir in dir_structure[dir_name]["subdir"]:
        print(sub_dir)
        size += get_dir_size(sub_dir)
    return size


for key in dir_structure:
    print(key, dir_structure[key])

print(dir_structure["zmj"])
print(get_dir_size("zmj"))

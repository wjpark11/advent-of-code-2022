import re
from collections import defaultdict

with open("day7_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines()]

dir_structure = defaultdict(lambda: {"dir_path": [], "size": 0, "total_size": 0})
current_path = []
current_dir = ""
for line in inputs:
    if re.match(r"^\$\scd\s[^\.\s]*$", line):
        current_path.append(re.match(r"\$\scd\s([^\.\s]*)", line).group(1))
        current_dir = "/".join(current_path)
        dir_structure[current_dir]["dir_path"] = current_path.copy()
    elif line == "$ cd ..":
        current_path.pop()
        current_dir = "/".join(current_path)
    elif re.match(r"^\d+\s.*", line):
        dir_structure[current_dir]["size"] += int(re.match(r"^(\d+)\s.*", line).group(1))
    else:
        pass
    

for key in dir_structure:
    size_list = [v["size"] for k, v in dir_structure.items() if key in k]
    dir_structure[key]["total_size"] = sum(size_list)

available_space = 70000000 - dir_structure["/"]["total_size"]
required_space = 30000000 - available_space

deletable_dir_sizes = [v["total_size"] for k, v in dir_structure.items() if v["total_size"] >= required_space]

print(min(deletable_dir_sizes))
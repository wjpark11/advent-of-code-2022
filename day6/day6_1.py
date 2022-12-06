with open("day6_input.txt", "rt") as f:
    inputs = f.readlines()[0].strip()

for i, _ in enumerate(inputs):
    if len(set(inputs[i : i + 4])) == 4:
        print(i + 4)
        break

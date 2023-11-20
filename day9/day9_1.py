with open("day9_input.txt", "rt") as f:
    inputs = [(input.strip().split(" ")[0], int(input.strip().split(" ")[1])) for input in f.readlines()]

print(inputs)
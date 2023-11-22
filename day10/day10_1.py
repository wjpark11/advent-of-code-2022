with open("day10_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines()]

cycle = 0
register = 1

history = []

for signal in inputs:
    if signal == "noop":
        cycle += 1
        history.append([cycle, register])
    elif signal.startswith("addx"):
        num = int(signal.split()[1])
        cycle += 1
        history.append([cycle, register])
        cycle += 1
        history.append([cycle, register])
        register += num
    else:
        pass

total_strength = 0
for cycle, register in history:
    if cycle % 40 == 20:
        total_strength += cycle * register

print(total_strength)

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

lines = [[item[0] % 40 if item[0] % 40 else 40, item[1]] for item in history]
lines = [lines[40 * i : 40 * (i + 1)] for i in range(0, len(history) // 40)]


def to_crt(line):
    row = ""
    for item in line:
        sprite_range = range(item[1] - 1, item[1] + 2)
        position = item[0] - 1
        if position in sprite_range:
            row += "#"
        else:
            row += "."

    return row


for line in lines:
    print(to_crt(line))

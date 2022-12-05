import re

with open("day5_input.txt", "rt") as f:
    inputs = [input for input in f.readlines()]

matrix = []
for input in inputs[:8]:
    matrix.append([char for idx, char in enumerate(input) if idx % 4 == 1])


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)
    return matrix_T


stacks = [[char for char in row if char != " "] for row in transpose(matrix)]
for row in stacks:
    row.reverse()

procedures = [
    [int(char) for char in re.findall(r"\d+", input.strip())] for input in inputs[10:]
]

for procedure in procedures:
    [n, f, t] = procedure
    f -= 1
    t -= 1
    cargo = stacks[f][-1 * n :]
    cargo.reverse()
    stacks[f] = stacks[f][: -1 * n]
    stacks[t] += cargo

ans = [row[-1] for row in stacks]

print("".join(ans))

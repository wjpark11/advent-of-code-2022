with open("day12_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines()]

inputs = [[letter for letter in line] for line in inputs]

WIDTH = len(inputs[0])
HEIGHT = len(inputs)

matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())

for i, line in enumerate(inputs):
    for j, letter in enumerate(line):
        if letter == "S":
            matrix[i][j] = 0
            start_point = (i, j)
        elif letter == "E":
            matrix[i][j] = 25
            end_point = (i, j)
        else:
            matrix[i][j] = ALPHABET.index(letter)

visited = []


def get_neighbours(current_points, visited):
    neighbours = []
    for point in current_points:
        if (
            point[0] > 0
            and matrix[point[0] - 1][point[1]] <= matrix[point[0]][point[1]] + 1
            and (point[0] - 1, point[1]) not in visited
        ):
            neighbours.append((point[0] - 1, point[1]))
        if (
            point[0] < HEIGHT - 1
            and matrix[point[0] + 1][point[1]] <= matrix[point[0]][point[1]] + 1
            and (point[0] - 1, point[1]) not in visited
        ):
            neighbours.append((point[0] + 1, point[1]))
        if (
            point[1] > 0
            and matrix[point[0]][point[1] - 1] <= matrix[point[0]][point[1]] + 1
            and (point[0] - 1, point[1]) not in visited
        ):
            neighbours.append((point[0], point[1] - 1))
        if (
            point[1] < WIDTH - 1
            and matrix[point[0]][point[1] + 1] <= matrix[point[0]][point[1]] + 1
            and (point[0] - 1, point[1]) not in visited
        ):
            neighbours.append((point[0], point[1] + 1))
    return neighbours

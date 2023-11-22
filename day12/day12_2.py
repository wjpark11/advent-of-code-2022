from math import inf

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


def get_neighbours(current_points, visited, matrix):
    neighbours = set()
    for point in current_points:
        if (
            point[0] > 0
            and matrix[point[0] - 1][point[1]] <= matrix[point[0]][point[1]] + 1
            and (point[0] - 1, point[1]) not in visited
        ):
            neighbours.add((point[0] - 1, point[1]))
        if (
            point[0] < HEIGHT - 1
            and matrix[point[0] + 1][point[1]] <= matrix[point[0]][point[1]] + 1
            and (point[0] + 1, point[1]) not in visited
        ):
            neighbours.add((point[0] + 1, point[1]))
        if (
            point[1] > 0
            and matrix[point[0]][point[1] - 1] <= matrix[point[0]][point[1]] + 1
            and (point[0], point[1]-1) not in visited
        ):
            neighbours.add((point[0], point[1] - 1))
        if (
            point[1] < WIDTH - 1
            and matrix[point[0]][point[1] + 1] <= matrix[point[0]][point[1]] + 1
            and (point[0], point[1]+1) not in visited
        ):
            neighbours.add((point[0], point[1] + 1))
    return neighbours, visited.union(current_points)


def get_distance(start_point, end_point, matrix):
    current_points = {start_point,}
    visited = set()

    distance = 0

    while True:
        current_points, visited = get_neighbours(current_points, visited, matrix)
        distance += 1
        if end_point in current_points:
            break
        elif not current_points:
            distance = inf
            break

    return distance

min_dist = inf
for i in range(HEIGHT):
    for j in range(WIDTH):
        if matrix[i][j] == 0:
            min_dist = min(min_dist, get_distance((i, j),end_point, matrix))

print(min_dist)

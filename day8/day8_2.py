with open("day8_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines()]

inputs = [[int(letter) for letter in input]for input in inputs]

def scenic_score(matrix, i, j):
    width = len(matrix[0])
    height = len(matrix)
    tree_height = matrix[i][j]

    if i in (0, height - 1) or j in (0, width - 1):
        return 0
    
    top_trees = matrix[i][:j][::-1]
    down_trees = matrix[i][j+1:]
    left_trees = [matrix[k][j] for k in range(i)][::-1]
    right_trees = [matrix[k][j] for k in range(i+1, height)]

    top_score = 0
    for height in top_trees:
        if height < tree_height:
            top_score += 1
        else:
            top_score += 1
            break

    down_score = 0
    for height in down_trees:
        if height < tree_height:
            down_score += 1
        else:
            down_score += 1
            break
    
    left_score = 0
    for height in left_trees:
        if height < tree_height:
            left_score += 1
        else:
            left_score += 1
            break

    right_score = 0
    for height in right_trees:
        if height < tree_height:
            right_score += 1
        else:
            right_score += 1
            break

    return top_score * down_score * left_score * right_score


max_scenic_score = 0

for i in range(len(inputs)):
    for j in range(len(inputs[0])):
        max_scenic_score = max(max_scenic_score, scenic_score(inputs, i, j))

print(max_scenic_score)
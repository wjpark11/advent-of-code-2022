with open("day8_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines()]

inputs = [[int(letter) for letter in input]for input in inputs]

def is_visible(matrix, i, j):
    width = len(matrix[0])
    height = len(matrix)
    tree_height = matrix[i][j]

    if i in (0, height - 1) or j in (0, width - 1):
        return True
    
    if max(matrix[i][:j]) < tree_height:
        return True
    if max(matrix[i][j+1:]) < tree_height:
        return True
    if max([matrix[k][j] for k in range(i)]) < tree_height:
        return True
    if max([matrix[k][j] for k in range(i+1, height)]) < tree_height:
        return True
    
    return False

visible_tree_num = 0

for i in range(len(inputs)):
    for j in range(len(inputs[0])):
        if is_visible(inputs, i, j):
            visible_tree_num += 1

print(visible_tree_num)
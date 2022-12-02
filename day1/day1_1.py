with open("day1_input.txt", "rt") as f:
    inputs = f.readlines()
    # inputs = [int(input.strip()) for input in inputs]

def day1_1(inputs):
    max_val = 0
    temp_sum = 0
    for input in inputs:
        if input != "\n":
            temp_sum += int(input.strip())
        else:
            max_val = max(max_val, temp_sum)
            temp_sum = 0
    return max_val



if __name__ == "__main__":
    print(day1_1(inputs))
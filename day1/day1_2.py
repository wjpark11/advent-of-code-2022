with open("day1_input.txt", "rt") as f:
    inputs = f.readlines()
    # inputs = [int(input.strip()) for input in inputs]

def day1_2(inputs):
    max_vals = [0, 0, 0]
    temp_sum = 0
    for input in inputs:
        if input != "\n":
            temp_sum += int(input.strip())
        else:
            if temp_sum >= max_vals[0]:
                max_vals[0] = temp_sum
                max_vals.sort()
            temp_sum = 0
    return sum(max_vals)



if __name__ == "__main__":
    print(day1_2(inputs))
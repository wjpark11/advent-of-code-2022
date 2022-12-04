import re
from readinputs import read_inputs


inputs = read_inputs("day4_input.txt")


def day4_1(inputs):
    full_contains = 0
    for pair in inputs:
        nums = re.findall(r"\d+", pair)
        if int(nums[0]) > int(nums[2]):
            if int(nums[3]) >= int(nums[1]):
                full_contains += 1
        elif int(nums[0]) < int(nums[2]):
            if int(nums[3]) <= int(nums[1]):
                full_contains += 1
        else:
            full_contains += 1
    return full_contains


if __name__ == "__main__":
    print(day4_1(inputs))

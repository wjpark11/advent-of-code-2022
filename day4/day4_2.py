import re
from readinputs import read_inputs


inputs = read_inputs("day4_input.txt")


def day4_2(inputs):
    overlapping_pairs = 0
    for pair in inputs:
        [p1_s, p1_e, p2_s, p2_e] = re.findall(r"\d+", pair)
        if int(p1_s) > int(p2_s):
            if int(p2_e) >= int(p1_s):
                overlapping_pairs += 1
        elif int(p1_s) < int(p2_s):
            if int(p1_e) >= int(p2_s):
                overlapping_pairs += 1
        else:
            overlapping_pairs += 1
    return overlapping_pairs


if __name__ == "__main__":
    print(day4_2(inputs))

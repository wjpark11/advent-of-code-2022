with open("day3_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

def char_score(char):
    if ord(char) < 97:
        score = ord(char) - 38
    else:
        score = ord(char) - 96
    return score


def day3_1(inputs):
    items = []
    for input in inputs:
        length = int(len(input)/2)
        first_half = input[:length]
        second_half = input[length:]
        both = set(first_half).intersection(set(second_half)).pop()
        items.append(both)

    sum = 0
    for char in items:
        sum += char_score(char)

    return sum


if __name__ == "__main__":
    print(day3_1(inputs))
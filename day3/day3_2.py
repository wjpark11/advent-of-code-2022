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
    i = 0
    sum = 0
    while True:
        group = inputs[i * 3 : (i + 1) * 3]
        badge = (
            set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        )
        sum += char_score(badge)
        i += 1
        if i * 3 >= len(inputs):
            break

    return sum


if __name__ == "__main__":
    print(day3_1(inputs))

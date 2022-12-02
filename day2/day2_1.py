with open("day2_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


def day2_1(inputs):
    score_dict = {
        "A X": 1+3,
        "A Y": 2+6,
        "A Z": 3+0,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 1+6,
        "C Y": 2+0,
        "C Z": 3+3,
    }
    score = 0
    for input in inputs:
        if input:
            score += score_dict[input]
    return score



if __name__ == "__main__":
    print(day2_1(inputs))
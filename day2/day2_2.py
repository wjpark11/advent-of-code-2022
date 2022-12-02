with open("day2_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]


def day2_2(inputs):
    score_dict = {
        "A X": 0+3,
        "A Y": 3+1,
        "A Z": 6+2,
        "B X": 0+1,
        "B Y": 3+2,
        "B Z": 6+3,
        "C X": 0+2,
        "C Y": 3+3,
        "C Z": 6+1,
    }
    score = 0
    for input in inputs:
        if input:
            score += score_dict[input]
    return score



if __name__ == "__main__":
    print(day2_2(inputs))
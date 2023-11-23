with open("day13_input.txt", "rt") as f:
    inputs = [input.strip() for input in f.readlines() if input.strip() != ""]

packets = []
for i, line in enumerate(inputs):
    if i % 2 == 0:
        packets.append({"left": eval(line), "right": eval(inputs[i + 1])})


def is_right_order(left: list, right: list) -> bool:
    if left and not right:
        return False
    if not left and right:
        return True
    if not left and not right:
        if isinstance(left[1], list) and isinstance(right[1], list):
            return is_right_order(left[1], right[1])

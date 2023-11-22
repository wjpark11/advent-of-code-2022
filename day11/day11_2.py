monkeys = [
    {"items": [98, 97, 98, 55, 56, 72], "inspects": 0},
    {"items": [73, 99, 55, 54, 88, 50, 55], "inspects": 0},
    {"items": [67, 98], "inspects": 0},
    {"items": [82, 91, 92, 53, 99], "inspects": 0},
    {"items": [52, 62, 94, 96, 52, 87, 53, 60], "inspects": 0},
    {"items": [94, 80, 84, 79], "inspects": 0},
    {"items": [89], "inspects": 0},
    {"items": [70, 59, 63], "inspects": 0},
]


def inspect(monkey_num: int) -> bool:
    remainder_num = 11 * 17 * 5 * 13 * 19 * 2 * 3 * 7
    if not monkeys[monkey_num]["items"]:
        return False

    worry_level = monkeys[monkey_num]["items"][0]

    if monkey_num == 0:
        worry_level *= 13
        worry_level = worry_level % remainder_num

        if worry_level % 11 == 0:
            monkeys[4]["items"].append(worry_level)
        else:
            monkeys[7]["items"].append(worry_level)

    elif monkey_num == 1:
        worry_level += 4
        worry_level = worry_level % remainder_num

        if worry_level % 17 == 0:
            monkeys[2]["items"].append(worry_level)
        else:
            monkeys[6]["items"].append(worry_level)

    elif monkey_num == 2:
        worry_level *= 11
        worry_level = worry_level % remainder_num

        if worry_level % 5 == 0:
            monkeys[6]["items"].append(worry_level)
        else:
            monkeys[5]["items"].append(worry_level)

    elif monkey_num == 3:
        worry_level += 8
        worry_level = worry_level % remainder_num

        if worry_level % 13 == 0:
            monkeys[1]["items"].append(worry_level)
        else:
            monkeys[2]["items"].append(worry_level)

    elif monkey_num == 4:
        worry_level *= worry_level
        worry_level = worry_level % remainder_num

        if worry_level % 19 == 0:
            monkeys[3]["items"].append(worry_level)
        else:
            monkeys[1]["items"].append(worry_level)

    elif monkey_num == 5:
        worry_level += 5
        worry_level = worry_level % remainder_num

        if worry_level % 2 == 0:
            monkeys[7]["items"].append(worry_level)
        else:
            monkeys[0]["items"].append(worry_level)

    elif monkey_num == 6:
        worry_level += 1
        worry_level = worry_level % remainder_num

        if worry_level % 3 == 0:
            monkeys[0]["items"].append(worry_level)
        else:
            monkeys[5]["items"].append(worry_level)

    elif monkey_num == 7:
        worry_level += 3
        worry_level = worry_level % remainder_num

        if worry_level % 7 == 0:
            monkeys[4]["items"].append(worry_level)
        else:
            monkeys[3]["items"].append(worry_level)

    monkeys[monkey_num]["inspects"] += 1
    monkeys[monkey_num]["items"].pop(0)

    return True


for _ in range(10000):
    for i in range(8):
        remained = True
        while remained:
            remained = inspect(i)

inspects = [monkey["inspects"] for monkey in monkeys]

inspects.sort(reverse=True)

print(inspects[0] * inspects[1])

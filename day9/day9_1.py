with open("day9_input.txt", "rt") as f:
    inputs = [(input.strip().split(" ")[0], int(input.strip().split(" ")[1])) for input in f.readlines()]

HEAD_WALKS = "".join([walk[0]*walk[1] for walk in inputs])

def get_head_position(head_x, head_y, walk):
    if walk == "U":
        return head_x, head_y + 1
    if walk == "D":
        return head_x, head_y - 1
    if walk == "R":
        return head_x + 1, head_y
    if walk == "L":
        return head_x - 1, head_y
    raise ValueError("Invalid walk")


def set_tail_position(head_x, head_y, tail_x, tail_y):
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail_x, tail_y
    if head_x == tail_x:
        if head_y > tail_y:
            return tail_x, tail_y + 1
        else:
            return tail_x, tail_y - 1
    if head_y == tail_y:
        if head_x > tail_x:
            return tail_x + 1, tail_y
        else:
            return tail_x - 1, tail_y
    if abs(head_x - tail_x) == 2:
        tail_y = head_y
        if head_x > tail_x:
            return tail_x + 1, tail_y
        else:
            return tail_x - 1, tail_y
    if abs(head_y - tail_y) == 2:
        tail_x = head_x
        if head_y > tail_y:
            return tail_x , tail_y + 1
        else:
            return tail_x , tail_y - 1
    raise ValueError("Invalid head and tail position")

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
tail_visited_point = {(0, 0),}

for walk in HEAD_WALKS:
    head_x, head_y = get_head_position(head_x, head_y, walk)
    tail_x, tail_y = set_tail_position(head_x, head_y, tail_x, tail_y)
    tail_visited_point.add((tail_x, tail_y))

print(len(tail_visited_point))

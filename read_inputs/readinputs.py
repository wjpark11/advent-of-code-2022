def read_inputs(file: str, is_int: bool = False) -> list:
    with open("day3_input.txt", "rt") as f:
        inputs = f.readlines()
        inputs = [input.strip() for input in inputs]
    return inputs

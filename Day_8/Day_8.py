# Advent of Code 2024 - Day 8

def open_file():
    contents = []
    with open("./test_input.txt", "r") as file:
        for line in file.readlines():
            res, ops = line.split(":")
            operands = ops.strip().split(" ")
            contents.append([int(res), list(map(int, operands))])
    return contents


if __name__ == "__main__":
    solve(True)
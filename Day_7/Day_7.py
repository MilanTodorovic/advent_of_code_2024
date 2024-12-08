# Advent of Code 2024 - Day 7
from copy import deepcopy
from itertools import product

ARITHMETICS = {"*": lambda x,y: x*y, "+": lambda x,y: x+y, "-": lambda x,y: x-y, "/": lambda x,y: x//y, "|": lambda x,y: str(x)+str(y)}


def open_file():
    contents = []
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            res, ops = line.split(":")
            operands = ops.strip().split(" ")
            contents.append([int(res), list(map(int, operands))])
    return contents


def make_operators(lenght):
    # OBSOLETE AND DOESN'T WORK QUITE RIGHT
    m = list("*" * (lenght))
    a = list("+" * (lenght))
    r = [deepcopy(m), deepcopy(a)]

    # First loop i=0:
    # [+,*,*,*,*]
    # [+,+,*,*,*]
    #   ...
    # Second loop i=1:
    # [*,+,*,*,*]
    # [*,+,+,*,*]
    l = len(m)
    for i in range(l):
        _m = deepcopy(m)
        _a = deepcopy(a)
        for j in range(i,l):
            _m[j] = "+"
            _a[j] = "*"
            r.append(deepcopy(_m))
            r.append(deepcopy(_a))

    # some combinations are missing?
    for c in deepcopy(r):
        if not c[::-1] in r:
            r.append(c[::-1])
    
    k = set()

    # remove duplicates from reversing
    for c in r:
        k.add("".join(c))

    r = [list(c) for c in k]

    #print("\n".join("".join(_) for _ in r))

    return r


def solve(part_two=False):
    results = []
    numbers = open_file()

    for calculations in numbers:
        expected = calculations[0]
        operands = calculations[1]
        if part_two:
            operators = list(product("+*|",repeat=len(operands)-1))
        else:
            operators = list(product("+*",repeat=len(operands)-1))

        solved = False

        for comb in operators:
            if solved:
                break
            # make a fresh copy of the operands to pop
            op = deepcopy(operands)
            for c in comb:
                # take the first TWO operands and perfrom arithmetic opperation
                calc = int(ARITHMETICS[c](op.pop(0), op.pop(0)))
                # put the calculation result as the first operand for the next iteration
                op = [calc] + op
                #print(op)
                if len(op) == 1:
                    if expected == calc:
                        print("Found solution for", expected)
                        results.append(expected)
                        solved = True
                        break
        else:
            pass
            #print("No sloution for ", expected)

    print("Total callibration result:", sum(results)) # 6392012777720 good, 61561126043536 low


def part_two():
    numbers = open_file()


if __name__ == "__main__":
    solve(True)
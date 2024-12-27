# Advent of Code 2024 - Day 24
# Dunno how to do Part two :'-(

from collections import defaultdict

FILE = ""
GATES = defaultdict(list)
OPERATORS = {"AND": lambda x,y: x and y, "OR": lambda x,y: x or y, "XOR": lambda x,y: (x or y) and (not (x and y))}
WIRES = {}
RESULT_WIRES = []


def open_file():
    global GATES, WIRES, RESULT_WIRES

    _gates = False
    with open(FILE, "r") as file:
        for line in file.readlines():
            if line == "\n":
                _gates = True
                continue
            if _gates:
                w1, op, w2, _, w3 = line.strip().split(" ")
                if w3[0] == "z":
                    RESULT_WIRES.append(w3) 
                GATES[op].append([w1, w2, w3])
                WIRES[w1] = WIRES.get(w1, None)
                WIRES[w2] = WIRES.get(w2, None)
                WIRES[w3] = WIRES.get(w3, None)
            else:
                # wire with value x01: 1
                w, v = [x.strip() for x in line.strip().split(":")]
                WIRES[w] = int(v)
        RESULT_WIRES.sort(reverse=True)


def solve():
    global WIRES

    while True:
        for op, ws in GATES.items():
            for w in ws:
                _ = OPERATORS[op](WIRES[w[0]], WIRES[w[1]])
                # i suspect XOR returns bool so we convert it
                WIRES[w[2]] = _ if _ is None else int(_)
        for wire in RESULT_WIRES:
            if WIRES[wire] is not None:
                continue
            else:
                # exit for-loop and continue with evaluating wires
                break
        else:
            # all result wires have a value
            break

    tmp = ""
    for wire in RESULT_WIRES:
        tmp += str(WIRES[wire])
    
    print("Result:", int(tmp,2)) # 51107420031718, 


if __name__ == "__main__":
    test = False
    if test:
        FILE = "./test_input.txt"
    else:
        FILE = "./input.txt"
    open_file()
    solve()
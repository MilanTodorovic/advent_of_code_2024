# Advent of Code 2024 - Day 9


def open_file():
    contents = ""
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            contents = line.strip()
    return contents


def decode_string():
    pass


def solve(part_two=False):
    available_space = []
    lst = []
    dct = {}
    _id = 0
    checksum = open_file()
    # if there is no empty space after the last block, it is NOT denoted
    if len(checksum) % 2 == 1:
        # adding hte trailing zero just to make things easier
        checksum += "0"
    
    for i in range(0,len(checksum),2):
        block_id, block, empty_space = _id, checksum[i], checksum[i+1]
        _id += 1
        # decoded string
        dct[block_id] = str(block_id) * int(block) + "." * int(empty_space)
        lst.extend([str(block_id)]*int(block))
        lst.extend(["."] * int(empty_space))

    if not part_two:
    # fill empty space by moving numbers from the back to the front
        for i in range(len(lst)-1,-1, -1):
            dot = lst.index(".")
            if dot > i:
                # remove trailing dots
                lst = lst[:dot]
                break
            lst[dot], lst[i] = lst[i], lst[dot]
    else:
        # fill empty space by moving whole blocks from the back to the front
        j = 0
        print("'.' found at:", lst.index(".", j))
        dot = lst.index(".", j)
        for k in range(dot, len(lst)):
            while k<len(lst):
                if lst[k] == ".":
                    k += 1
                else:
                    j = k + 1
                    # available space at index i
                    available_space.append((dot, j))
                    break
        print("Space:", available_space[:10])

    # calculate new chechsum
    if not part_two:
        new_checksum = 0
        for i in range(len(lst)):
            new_checksum += i*int(lst[i])
        print(new_checksum)
    else:
        #new_checksum = 0
        #for i in range(len(lst)):
        #    new_checksum += i*int(lst[i])
        #print(new_checksum)
        pass


if __name__ == "__main__":
    #solve() # 6201130364722
    solve(True) # 
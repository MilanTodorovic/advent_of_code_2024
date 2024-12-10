# Advent of Code 2024 - Day 9


def open_file():
    contents = ""
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            contents = line.strip()
    return contents


def solve(part_two=False):
    blocks = [] # (size, index) will be reversed for easier iteration
    available_space = [] # (size, index)
    lst = []
    checksum = open_file()

    # if there is no empty space after the last block, it is NOT denoted
    if len(checksum) % 2 == 1:
        # adding hte trailing zero just to make things easier
        checksum += "0"
    
    _id = 0
    block_index = 0
    space_index = 0
    for i in range(0,len(checksum),2):
        block_id, block_size, space_size = _id, int(checksum[i]), int(checksum[i+1])
        block = [str(block_id)]*block_size
        block_data = (block,block_index)
        blocks.append(block_data)
        lst.extend(block) # for part one
        #lst.append(block)
        if space_size:
            # space index starts after a block: [9,9] at i=2 -> i=4 since [9,9] is index 2 and 3
            space_index = block_index+block_size
            available_space.append((space_size,space_index))
            lst.extend(["."] * space_size)
        else:
            space_index = block_index+block_size
        #print(f"{block_id}. block:{block_size} - space:{space_size}")
        #print(f"\tBlock: {block} at {block_index}")
        #print(f"\tSpace: {space_size} at {space_index}")
        # new block starts right after the last empty space
        block_index = space_index+space_size
        #print("Block_index=", block_index)
        # increment block_id
        _id += 1

    if not part_two:
    # fill empty space by moving numbers from the back to the front
        for i in range(len(lst)-1,-1,-1):
            dot = lst.index(".")
            if dot > i:
                # remove trailing dots
                lst = lst[:dot]
                break
            lst[dot], lst[i] = lst[i], lst[dot]
    else:
        # Part two of the puzzle
        # fill empty space by moving whole blocks from the back to the front
        #print("Before:", lst)
        for block_data in blocks[::-1]:
            block, block_index = block_data
            block_size = len(block)
            #print(f"Trying to move {block}")

            for i, space in zip(range(len(available_space)), available_space):
                space_size, space_index = space

                if block_size <= space_size:
                    #print(f"Block {block} is less then the space available at {space_index}:{space_index+space_size}")

                    if block_index > space_index:
                        #print(f"Block {block} index is {block_index} and space has index {space_index}")
                        start = space_index
                        end = space_index + block_size
                        _start = block_index
                        _end = block_index+block_size
                        #print(f"Block {lst[_start:_end]} being moved to {lst[start:end]}")

                        # swap positions 
                        lst[start:end], lst[_start:_end] = lst[_start:_end], lst[start:end]
                        remaining_space = space_size-block_size

                        if remaining_space:
                            available_space[i] = (remaining_space, space_index+block_size)
                            #print("Remaing space", remaining_space, available_space[i])
                        else:
                            available_space.pop(i)
                        break

                    else:
                        #print(f"Unable to move block {block} to {lst[space_index:space_size]}.")
                        break
                else:
                    #print(f"Block {block} is greater than {lst[space_index:space_size]}")
                    pass
            #print(lst)
        #print("After:", lst)

    # calculate new chechsum
    if not part_two:
        new_checksum = 0
        for i in range(len(lst)):
            new_checksum += i*int(lst[i])
        print("Part one checksum:", new_checksum)
    else:
        new_checksum = 0
        for i in range(len(lst)):
            if lst[i] == ".":
                continue
            new_checksum += i*int(lst[i])
        print("Part two checksum:", new_checksum)


if __name__ == "__main__":
    #solve() # 6201130364722
    solve(True) # 
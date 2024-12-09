# Advent of Code 2024 - Day 8
from collections import defaultdict
from copy import deepcopy
import math

GRID = None
EMPTY_TILE = "."

def open_file():
    contents = []
    with open("./test_input.txt", "r") as file:
        for line in file.readlines():
            contents.append(line.strip())
    return contents


def calculate_vectors(a,b):
    return (a[0]-b[0], a[1]-b[1])


def claculate_antinode(a,b,distance):
    # Vector distance:
    #   (+1,+1) - a+(-1,-1), b+(+1,+1)
    #   (-1,+1) - a+(+1,-1), b+(-1,+1)
    #   (+1,-1) - a+(-1,+1), b+(+1,-1)
    #   (-1,-1) - a+(+1,+1), b+(-1,-1)
    x = distance[0]
    y = distance[1]
    if x > 0 and y > 0:
        a = tuple(map(sum,zip(a,(x,y))))
        b = tuple(map(sum,zip(b,(-x,-y))))
    elif x < 0 and y > 0:
        a = tuple(map(sum,zip(a,(-x,y))))
        b = tuple(map(sum,zip(b,(x,-y))))
    elif x > 0 and y < 0:
        a = tuple(map(sum,zip(a,(x,-y))))
        b = tuple(map(sum,zip(b,(-x,y))))
    else:
        # both x and y < 0
        a = tuple(map(sum,zip(a,(x,y))))
        b = tuple(map(sum,zip(b,(-x,-y))))
    return [a,b]



def make_increment(distance, increment):
    x, y = distance
    _x,_y = increment
    if x >= 0 and y >= 0:
        return (-_x,-_y)
        #return (_x,_y)
    elif x <= 0 and y >= 0:
        return (_x,-_y)
        #return (-_x,_y)
    elif x >= 0 and y <= 0:
        return (-_x,_y)
        #return (_x,-_y)
    else:
        # both x and y < 0
        return (_x,_y)
        #return (-_x,-_y)


def is_obstructed(start, end, increment, char):
    print("Checking for obstruction.")
    print(f"Start={start}, end={end}, increment={increment}, char={char}")
    checkpoint = None
    while True:
        checkpoint = tuple(map(sum,zip(start,increment)))
        print("Checkpoint", checkpoint)
        if checkpoint == end:
            return False
        if GRID[checkpoint[0]][checkpoint[1]] in [EMPTY_TILE, char]:
            continue
        else:
            return True
    return False


def solve(part_two=False):
    global GRID
    unique_chars = defaultdict(list)
    antinodes = []
    result = 0
    GRID = open_file()
    _GRID = deepcopy(GRID)
    overlay = [list(row) for row in _GRID]
    max_row = len(GRID)
    max_col =  len(GRID[0])

    for i, row in zip(range(max_row), GRID):
        for j, col in zip(range(max_col), row):
            if col.isalnum():
                unique_chars[col].append((i,j))
    print(unique_chars)

    for k, v in unique_chars.items():
        char = k
        _v = deepcopy(v)
        
        while len(_v)>1:
            main_coord = _v.pop(0)
            for coord in _v:
                print(f"{char} - {main_coord} - {coord}")
                distance = calculate_vectors(main_coord, coord)

                # P.S. x=row, y=column
                # P.P.S. Check bot -1 and +1, -2 and +2
                # Few base cases:
                #   (x,0) - check every (1,0)
                #   (0,y) - check every (0,1)
                #   (1,1) - all good
                #   (2,2) - x==y - check every (1,1)
                #   (1,2) - x*2==y, y%2==0 - check every (1,2)
                #   (2,1) - y*2==x, x%2==0 - check every (2,1)
                #   (5,3) - x and y both prime - check every (x,y)
                x = distance[0]
                y = distance[1]
                if x == 0 or y == 0:
                    if x:
                        obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(1,0)), char)
                    else:
                        obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(0,1)), char)
                elif abs(x) == 1 and abs(y) == 1:
                    # can't be obstructed
                    obstructed = False
                elif abs(x) == abs(y):
                    # square, check every (+1,+1)
                    obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(1,1)), char)
                # might be a problem if there is a soution 2.01...
                elif abs(x) * 2 == abs(y) and abs(y) % 2 == 0:
                    #obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(2,1)), char)
                    obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(1,2)), char)
                elif abs(y) * 2 == abs(y) and abs(x) % 2 == 0:
                    #obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(2,1)), char)
                    obstructed = is_obstructed(main_coord, coord, make_increment((x,y),(1,2)), char)
                else:
                    # both prime numbers
                    obstructed = False
                    
                if not obstructed:
                    antinodes.extend(claculate_antinode(main_coord,coord,distance))
    print(antinodes)
    for antinode in antinodes:
        if (antinode[0]>=0 and antinode[0]<max_row) and (antinode[1]>=0 and antinode[1]<max_col):
            overlay[antinode[0]][antinode[1]] = "#"
            result += 1
    for row in overlay:
        print("".join(col for col in row))
    print(result)


if __name__ == "__main__":
    solve(True)
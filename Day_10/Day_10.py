# Advent of Code 2024 - Day 10
import sys

MAX_ROW = 0
MAX_COL = 0
VISITED_TILES = [] # eliminate paths that converge and then merge before 9
PART_TWO = False


def open_file():
    content = None
    with open("./input.txt", "r") as file:
        content = [line.strip() for line in file.readlines()]
    return content


def get_starting_locations(_map):
    _locations = []
    
    # no more zips and lens
    i, j = 0, 0
    for row in _map:
        for col in row:
            if col == "0":
                _locations.append((i,j))
            j+=1
        j=0
        i+=1

    return _locations


def get_valid_directions(_x, _y):
    N, S, E, W = 0, 0, 0, 0

    if _x < MAX_ROW-1:
        S = _x + 1
    if _x > 1 :
        N = _x - 1
    if _y < MAX_COL-1:
        E= _y + 1
    if _y > 1:
        W = _y - 1

    return [N,S,E,W]


def traverse(_previous, _current, _map):
    global VISITED_TILES

    if _current[0] == MAX_ROW or _current[0] < 0:
        return 0
    if _current[1] == MAX_COL or _current[1] < 0:
        return 0
    
    _t = _map[_current[0]][_current[1]]
    # for some test inputs only
    if _t == ".":
        return 0
    _t = int(_t)
    
    if _previous+1 == _t:
        if _t == 9:
            if _current not in VISITED_TILES:
                if not PART_TWO:
                    VISITED_TILES.append(_current)
                return 1
            else:
                return 0
        else:
            if _current not in VISITED_TILES:
                if not PART_TWO:
                    VISITED_TILES.append(_current)
            else:
                return 0
            x, y = _current[0], _current[1]
            return traverse(_t, (x+1,y), _map) + traverse(_t, (x-1,y), _map) + traverse(_t, (x,y+1), _map) + traverse(_t, (x,y-1), _map)
    else:
        return 0


def find_path(_start, _map):
    result = 0
    result += traverse(-1, _start, _map)
    #print(f"Path {_start} has a score of {result}.")
    return result


def solve(part_two=False):
    global MAX_ROW, MAX_COL, VISITED_TILES, PART_TWO
    
    if part_two:
        PART_TWO=True

    topographic_map = open_file()
    MAX_ROW = len(topographic_map)
    MAX_COL = len(topographic_map[0])
    starting_locations = get_starting_locations(topographic_map)

    # A*? Breadth-first? Flood? Time will tell
    sum_of_scores = 0
    for start in starting_locations:
        VISITED_TILES = []
        sum_of_scores += find_path(start, topographic_map)

    print("The sum of all path scores is", sum_of_scores)


if __name__ == "__main__":
    sys.setrecursionlimit(1000)
    #solve() # 644
    solve(True)
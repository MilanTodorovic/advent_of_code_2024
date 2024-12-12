# Advent of Code 2024 - Day 12
from collections import defaultdict
import sys


PART_TWO = False
MAX_ROW = 0
MAX_COL = 0
VISITED = defaultdict(list)
CURRENT = defaultdict(list) # data about the current plot of plants. Is deleted when we move to another plant
PLOT_PERIMETERS = defaultdict(list) # plant: [(,),...] perimeters. Is deleted when we move to another plant
TOTAL_PRICE = 0


def open_file():
    contents = None
    with open("./input.txt", "r") as file:
        contents = [line.strip() for line in file.readlines()]
    return contents


def traverse(garden, current_plant, start):
    global PLOT_PERIMETERS, VISITED
    
    if start in VISITED[current_plant] or start in CURRENT[current_plant]:
        return 0

    VISITED[current_plant].append(start)
    CURRENT[current_plant].append(start)

    N = (start[0]-1,start[1])
    E = (start[0],start[1]+1)
    S = (start[0]+1,start[1])
    W = (start[0],start[1]-1)

    # if out of bounds - we still need a fence
    if N[0] < 0:
        PLOT_PERIMETERS[current_plant].append(N)
    elif current_plant!=garden[N[0]][N[1]]:
        PLOT_PERIMETERS[current_plant].append(N)
    else:
        if N not in VISITED[current_plant]:
            traverse(garden, current_plant, N)

    if E[1] == MAX_COL:
        PLOT_PERIMETERS[current_plant].append(E)
    elif current_plant!=garden[E[0]][E[1]]:
        PLOT_PERIMETERS[current_plant].append(E)
    else:
        if E not in VISITED[current_plant]:
            traverse(garden, current_plant, E)

    if S[0] == MAX_ROW:
        PLOT_PERIMETERS[current_plant].append(S)
    elif current_plant!=garden[S[0]][S[1]]:
        PLOT_PERIMETERS[current_plant].append(S)
    else:
        if S not in VISITED[current_plant]:
            traverse(garden, current_plant, S)

    if W[1] < 0:
        PLOT_PERIMETERS[current_plant].append(W)
    elif current_plant!=garden[W[0]][W[1]]:
        PLOT_PERIMETERS[current_plant].append(W)
    else:
        if W not in VISITED[current_plant]:
            traverse(garden, current_plant, W)


def nr_of_sides(plant):
    # sort by row, then by column
    # check for continuity rows (138,139...), then columns
    
    sides = 0
    perimeters = PLOT_PERIMETERS[plant]
    # just one letter
    if len(perimeters) == 4:
        return 4
    
    perimeters.sort()
    # pick the the last bottom left coordinate and walk from there

    print(plant, ":", perimeters)
    for i in range(len(perimeters)-1):
        if perimeters[i][0] == perimeters[i+1][0]:
            if perimeters[i][1] == perimeters[i+1][1]:
                sides += 1
            
    perimeters.sort(key=lambda x: x[1])
    print(plant, ":", perimeters)
    return sides


def solve():
    global MAX_ROW, MAX_COL, COST, TOTAL_PRICE

    garden = open_file()
    MAX_ROW = len(garden)
    MAX_COL = len(garden[0])

    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            current_plant = garden[i][j]
            start = (i,j)
            if start not in VISITED[current_plant]:
                traverse(garden, current_plant, start)
                if PART_TWO:
                    sides = nr_of_sides(current_plant)
                    cost = len(CURRENT[current_plant])
                    cost *= sides
                    TOTAL_PRICE += cost
                    #print(f"The cost of {current_plant} is {cost}.")
                else:
                    cost = len(CURRENT[current_plant])
                    cost *= len(PLOT_PERIMETERS[current_plant])
                    TOTAL_PRICE += cost
                    print(f"The cost of {current_plant} is {cost}.")
                del CURRENT[current_plant]
                del PLOT_PERIMETERS[current_plant]
    
    print("Teh totsal price is:", TOTAL_PRICE) # 1361494, 

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    PART_TWO = True
    solve()
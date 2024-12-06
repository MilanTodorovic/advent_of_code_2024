# Advent of Code 2024 - Day 6
from dataclasses import dataclass
import re


@dataclass
class Guard():
	position: tuple
	facing: int

@dataclass
class Direction:
	N = 0
	E = 1
	S = 2
	W = 3

def open_file():
	with open("./input.txt", "r") as file:
		contents = [list(c.strip()) for c in file.readlines()]
		return contents

def traverse(grid, guard):
	visited_locations = 0
	obstacle = "#"
	on_grid = True
	_move = {Direction.N:(-1,0), Direction.E:(0,1), Direction.S:(1,0), Direction.W:(0,-1)}
	while on_grid:
		x = guard.position[0] + _move[guard.facing][0]
		y = guard.position[1] + _move[guard.facing][1]
		if (x < 0 or x == len(grid)) or (y < 0 or y == len(grid[0])):
			on_grid = False
			grid[guard.position[0]][guard.position[1]] = 'X'
		else:
			if grid[x][y] == obstacle:
				guard.facing = (guard.facing + 1) % 4
			else:
				grid[guard.position[0]][guard.position[1]] = 'X'
				guard.position = (x,y)
	for row in grid:
		visited_locations += "".join(row).count("X")

	print("visited locations:", visited_locations) # 5551


def part_one():
	contents = open_file()
	guard_position = (-1,-1)
	guard_direction = -1
	directions = {"^":Direction.N, ">":Direction.E, "v":Direction.S, "<":Direction.W}
	for i, c in zip(range(len(contents)), contents):
		j = re.search("\^|\>|\<|v", "".join(c)) # returns None if not found
		if j:
			guard_position = (i,j.start())
			guard_direction = directions[c[j.start()]]
			break

	guard = Guard(guard_position, guard_direction)
	traverse(contents, guard)

def part_two():
	pass



if __name__ == "__main__":
	part_one()
	part_two()
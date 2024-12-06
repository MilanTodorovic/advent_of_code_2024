# Advent of Code 2024 - Day 6
from dataclasses import dataclass
import re
import timeit
import copy

SUCCESSFUL_OBSTACLES = 0

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

_MOVE = {Direction.N:(-1,0), Direction.E:(0,1), Direction.S:(1,0), Direction.W:(0,-1)}
_MARK = {Direction.N:'↑', Direction.E:'→', Direction.S:'↓', Direction.W:'←'}

def open_file():
	with open("./input.txt", "r") as file:
		contents = [list(c.strip()) for c in file.readlines()]
		return contents


def traverse(grid, guard):
	global _MOVE
	visited_locations = 0
	obstacle = "#"
	on_grid = True
	while on_grid:
		x = guard.position[0] + _MOVE[guard.facing][0]
		y = guard.position[1] + _MOVE[guard.facing][1]
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


def get_path(grid, guard):
	global _MOVE
	guards_path = []
	obstacle = "#"
	on_grid = True

	while on_grid:
		x = guard.position[0] + _MOVE[guard.facing][0]
		y = guard.position[1] + _MOVE[guard.facing][1]
		if (x < 0 or x == len(grid)) or (y < 0 or y == len(grid[0])):
			on_grid = False
			guards_path.append((guard.position[0],guard.position[1]))
		else:
			if grid[x][y] in obstacle:
				guard.facing = (guard.facing + 1) % 4
			else:
				guards_path.append((guard.position[0],guard.position[1]))
				guard.position = (x,y)
	guards_path.pop(0) # remove the starting position as a possible obstacle location
	return guards_path


def traverse_and_mark(grid, guard_position, guard_direction, guards_path):
	global SUCCESSFUL_OBSTACLES, _MOVE, _MARK
	_guard = Guard(guard_position, guard_direction)
	_grid = copy.deepcopy(grid)
	obstacle = ["#", "O"]
	on_grid = True
	# add our obstacle
	_grid[guards_path[0]][guards_path[1]] = "O"

	while on_grid:
		x = _guard.position[0] + _MOVE[_guard.facing][0]
		y = _guard.position[1] + _MOVE[_guard.facing][1]
		if (x < 0 or x == len(_grid)) or (y < 0 or y == len(_grid[0])):
			on_grid = False
		else:
			if _grid[x][y] in obstacle:
				_guard.facing = (_guard.facing + 1) % 4
			else:
				u = _grid[_guard.position[0]][_guard.position[1]] 
				if u == ".":
					_grid[_guard.position[0]][_guard.position[1]]  = _MARK[_guard.facing]
				else:
					if _MARK[_guard.facing] != u:
						_grid[_guard.position[0]][_guard.position[1]] = "+"
					else:
						return 1
				_guard.position = (x,y)
	return 0


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
	global SUCCESSFUL_OBSTACLES
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
	guards_path = list(set(get_path(contents, guard)))

	s = []

	for path in guards_path:
		res = traverse_and_mark(contents, guard_position, guard_direction, path)
		s.append(res)

	print("Possible obstacles: ", sum(s))

if __name__ == "__main__":
	#start = timeit.default_timer()
	#part_one()
	#print("Part one in:", timeit.default_timer()-start)
	start = timeit.default_timer()
	part_two()
	print("Part two in:", timeit.default_timer()-start)
# Advent of Code 2024 - Day 14
import re
from collections import defaultdict
import math
import sys, os, time

PATTERN = "\=(-*\d+),(-*\d+)"
# X - columns, Y - rows
# robots warp around abs((P[.]+V[.]) % GRID_SIZE[.])
# robots can stack on each other
GRID_SIZE = None
FILE = None
MIDDLE = None
SECONDS = 0
ROBOTS = {}
NUMBER_OF_ROBOTS = 0

def open_file():
	global NUMBER_OF_ROBOTS

	contents = defaultdict(list)
	with open(FILE, "r") as file:
		i = 0
		for line in file.readlines():
			p,v = re.findall(PATTERN, line)
			# X - columns, Y - rows
			p = (int(p[0]), int(p[1]))
			v = (int(v[0]), int(v[1]))
			contents[i].extend([p,v])
			i += 1
		print("no. of robots:", i)
		NUMBER_OF_ROBOTS = i
	return contents


def draw_grid(i):
	grid  = [ [0]*GRID_SIZE[0] for i in range(GRID_SIZE[1])]
	string_grid = []

	for location in ROBOTS.values():
		loc = location[0]
		grid[loc[1]][loc[0]] += 1

	for g in grid:
		s = "".join(str(_) if _ > 0 else "." for _ in g)
		string_grid.append(s[:MIDDLE[0]]+" "+s[MIDDLE[0]+1:])
		#print(s)

	# remove middle
	#print("\nRemoved middle parts\n")
	#for i, s in zip(range(GRID_SIZE[1]), string_grid):
	#	if i == MIDDLE[1]:
	#		print(" "*GRID_SIZE[0])
	#		continue
	#	print(s)

	k = f"Iteration {i}\n"+"\n".join(s for s in string_grid)+"\n"
	os.system('clear')
	sys.stdout.write(k)
	sys.stdout.flush()
	#print(k, end='\r', flush=True)

def move():
	for robot, p_and_v in ROBOTS.items():
		_p = p_and_v[0]
		_v = p_and_v[1]
		_p = (abs((_p[0]+_v[0]) % GRID_SIZE[0]), abs((_p[1]+_v[1]) % GRID_SIZE[1]))
		ROBOTS[robot] = (_p, _v)
	#print(ROBOTS[0])


def solve():
	global ROBOTS

	ROBOTS = open_file()
	for i in range(SECONDS):
		print(f"Iteration {i}", end='\r', flush=True)
		move()

		# Indetned for part two
		robots_per_quad = {0:0, 1:0, 2:0, 3:0}

		for location in ROBOTS.values():
			loc = location[0]
			# Top left
			if loc[0] < MIDDLE[0] and loc[1] < MIDDLE[1]:
				robots_per_quad[0] += 1
			# horizontal or vertical middle
			elif loc[0] == MIDDLE[0] or loc[1] == MIDDLE[1]:
				# discard
				pass
			# Bottom right
			elif loc[0] > MIDDLE[0] and loc[1] < MIDDLE[1]:
				robots_per_quad[1] += 1
			# Bottom left
			elif loc[0] < MIDDLE[0] and loc[1] > MIDDLE[1]:
				robots_per_quad[2] += 1
			# Top right
			else:
				robots_per_quad[3] += 1

		for v in robots_per_quad.values():
			if v >= NUMBER_OF_ROBOTS//3:
				draw_grid(i) # 6354
				input("Press 0 to coitinue...")

	#print(robots_per_quad)
	if SECONDS == 100:
		print("Safty factor:", math.prod(robots_per_quad.values())) # 220971520


if __name__ == "__main__":
	test = False
	part_two = True

	if test:
		GRID_SIZE = (11,7)
		FILE = "./test_input.txt"
	else:
		GRID_SIZE = (101,103)
		FILE = "./input.txt"
	MIDDLE = (GRID_SIZE[0]//2, GRID_SIZE[1]//2)
	SECONDS = 100 if not part_two else 10000000
	solve()
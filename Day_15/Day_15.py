# Advent of Code 2024 - Day 15
from collections import defaultdict

MAP = []
STEPS = ""
FILE = ""
# (ROW, COL)
MOVE = {"^":(-1,0), ">":(0,+1), "v":(+1,0), "<":(0,-1)}
GRID_SIZE = None
BOX = "O"
WIDE_BOX = "[]"
WALL = "#"
ROBOT = "@"
FLOOR = "."
START = None
UPDATES = defaultdict(set)
PART_TWO = False


def double_everything(row):
	new_row = []
	for r in row:
		if r == ROBOT:
			new_row.extend([r, FLOOR])
		elif r == BOX:
			new_row.extend([WIDE_BOX[0], WIDE_BOX[1]])
		else:
			new_row.extend([r, r])
	return new_row


def open_file():
	global MAP, STEPS, GRID_SIZE, START
	flag = False
	i = 0
	with open(FILE, "r") as f:
		for line in f.readlines():
			if line == "\n":
				flag = True
			if flag:
				STEPS += line.strip()
			else:
				r = list(line.strip())
				if PART_TWO:
					r = double_everything(r)
				if ROBOT in r:
					START = (i,r.index(ROBOT))
				MAP.append(r)
				i += 1
	GRID_SIZE = len(MAP), len(MAP[0])


def move(start:tuple, step:tuple, who:str):
	global MAP, UPDATES

	next_row = start[0] + step[0]
	next_col = start[1] + step[1]
	
	if next_row < 0 or next_row > GRID_SIZE[0]:
		return False

	if next_col < 0 or next_col > GRID_SIZE[1]:
		return False

	next_tile = MAP[next_row][next_col]

	if next_tile == WALL:
		return False
	elif next_tile == BOX:
		result = move((next_row,next_col), step, BOX)
		if result:
			UPDATES[who].add((next_row, next_col))
			UPDATES[FLOOR].add(start)
			return True
		else:
			return False
	elif next_tile in WIDE_BOX:
		# both side have to be able to move
		# 3 boxes can now be aligned and moved all at once
		#	[][]
		#	 []

		if step == MOVES[">"] or step == MOVES["<"]:
			result = move((next_row,next_col), step, next_tile)
			if result:
				UPDATES[who].add((next_row, next_col))
				UPDATES[FLOOR].add(start)
				return True
			else:
				return False
		else:
			# movement is up/down and the side is either [ or ]
			if next_tile == WIDE_BOX[0]:
				n1 = (next_row,next_col)
				n2 = (next_row,next_col+1)
			else:
				n1 = (next_row,next_col-1)
				n2 = (next_row,next_col)
				
			r1 = move(n1, step, WIDE_BOX[0])
			if r1:
				r2 = move(n2, step, WIDE_BOX[1])
				if r2:
					UPDATES[who].add((next_row,next_col))
					UPDATES[FLOOR].add(start)
					return True
				else:
					return False
			else:
				return False
	else:
		UPDATES[who].add((next_row, next_col))
		UPDATES[FLOOR].add(start)
		return True


def start_moving():
	_start =  START
	# for-loop because sys.setrecursionlimit() is L A M E
	for step in STEPS:
		_r = move(_start, MOVES[step], ROBOT)
		if _r:
			for c in UPDATES[FLOOR]:
				MAP[c[0]][c[1]] = FLOOR
			for c in UPDATES[BOX]:
				MAP[c[0]][c[1]] = FLOOR
			for c in UPDATES[WIDE_BOX[0]]:
				MAP[c[0]][c[1]] = WIDE_BOX[0]
			for c in UPDATES[WIDE_BOX[1]]:
				MAP[c[0]][c[1]] = WIDE_BOX[1]
			for c in UPDATES[ROBOT]:
				MAP[c[0]][c[1]] = ROBOT
				_start = c
		UPDATES =defaultdict(set)


def calculate_distance():
	# 100 * ROW + COL
	total = 0
	i = 0 # row
	j = 0 # col
	for row in MAP:
		for col in row:
			if col == BOX or col == WIDE_BOX[0]:
				score = 100*i+j
				total += score
			j+=1
		i+=1
		j=0
	print("Total score:", total) # 1490942, 1519202


if __name__ == "__main__":
	# return all coordinates and then write the moves
	# dont do it if one is ok, but the rest isnt
	test = True # result should be 1216 for https://www.reddit.com/r/adventofcode/comments/1heoj7f/comment/m25oyt8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1
	PART_TWO = True
	if test:
		FILE = "./test_input.txt"
	else:
		FILE = "./input.txt"
	open_file()
	start_moving()
	calculate_distance()

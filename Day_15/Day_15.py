# Advent of Code 2024 - Day 15
import sys


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
	global MAP
	#print(start, step, who)
	next_row = start[0] + step[0]
	next_col = start[1] + step[1]
	
	if next_row < 0 or next_row > GRID_SIZE[0]:
		return start
	if next_col < 0 or next_col > GRID_SIZE[1]:
		return start

	next_tile = MAP[next_row][next_col]
	#print("Next tile is:", next_tile)

	if next_tile == WALL:
		return start
	elif next_tile == BOX:
		result = move((next_row,next_col), step, BOX)
		if result != (next_row,next_col):
			# box moved successfully
			MAP[next_row][next_col] = who
			MAP[start[0]][start[1]] = FLOOR
			return (next_row, next_col)
		else:
			return start
	elif next_tile in WIDE_BOX:
		# both side have to be able to move
		# 3 boxes can now be aligned and moved all at once
		#	[][]
		#	 []
		if next_tile == WIDE_BOX[0]: # [
			r1 = move((next_row,next_col), step, WIDE_BOX[0]) # left side
			r2 = move((next_row,next_col+1), step, WIDE_BOX[1]) # right side
			if r1 != (next_row,next_col) and r2 != (next_row,next_col+1):
				# box moved successfully
				MAP[next_row][next_col] = ROBOT
				MAP[start[0]][start[1]] = FLOOR
				return (next_row, next_col)
			else:
				return start
		# if who is [ and next is ]
		# so what?
		elif next_tile == WIDE_BOX[1] and who != WIDE_BOX[0]: # ]
			r1 = move((next_row,next_col-1), step, WIDE_BOX[0]) # left side
			r2 = move((next_row,next_col), step, WIDE_BOX[1]) # right side
			if r1 != (next_row,next_col-1) and r2 != (next_row,next_col):
				# box moved successfully
				MAP[next_row][next_col] = ROBOT
				MAP[start[0]][start[1]] = FLOOR
				return (next_row, next_col)
			else:
				return start
		# if next is ]
		else:
			r = move((next_row,next_col), step, WIDE_BOX[1]) # right side
			if r != (next_row,next_col):
				# box moved successfully
				MAP[next_row][next_col] = WIDE_BOX[1]
				MAP[start[0]][start[1]] = FLOOR
				return (next_row, next_col)
			else:
				return start
	else:
		if who in WIDE_BOX:
			if who == WIDE_BOX[0]:
				MAP[next_row][next_col+1] = WIDE_BOX[1]
				MAP[next_row][next_col] = who
				MAP[start[0]][start[1]] = FLOOR
				return (next_row, next_col)
			else:
				MAP[next_row][next_col-1] = WIDE_BOX[0]
				MAP[next_row][next_col] = who
				MAP[start[0]][start[1]] = FLOOR
				return (next_row, next_col)
		else:
			MAP[next_row][next_col] = who
			MAP[start[0]][start[1]] = FLOOR
			return (next_row, next_col)


def start_moving():
	_start =  START
	for row in MAP:
		print("".join(r for r in row))
	print("----------------------")
	# for-loop because sys.setrecursionlimit() is L A M E
	for step in STEPS:
		print(_start, step)
		_start = move(_start, MOVE[step], ROBOT)
		for row in MAP:
			print("".join(r for r in row))
		print("----------------------")


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
				#print(f"Box found at ({i},{j}) giving a score of {score}.\nTotal is {total}.")
			j+=1
		i+=1
		j=0
	print("Total score:", total)


if __name__ == "__main__":
	# well well well
	# if it isn't the trusty recursionlimit for part two
	sys.setrecursionlimit(100)
	test = True
	PART_TWO = True
	if test:
		FILE = "./test_input.txt"
	else:
		FILE = "./input.txt"
	open_file()
	start_moving()
	calculate_distance()

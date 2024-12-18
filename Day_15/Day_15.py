# Advent of Code 2024 - Day 15

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

	next_row = start[0] + step[0]
	next_col = start[1] + step[1]
	
	if next_row < 0 or next_row > GRID_SIZE[0]:
		return start
	if next_col < 0 or next_col > GRID_SIZE[1]:
		return start

	next_tile = MAP[next_row][next_col]

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

		if step == MOVE[">"] or step == MOVE["<"]:
			r = move((next_row,next_col), step, next_tile)
			if r != (next_row,next_col):
				MAP[next_row][next_col] = who
				MAP[start[0]][start[1]] = FLOOR
				return (next_row, next_col)
			else:
				return start
		else:
			# movement is up/down and the side is either [ or ]
			if next_tile == WIDE_BOX[0]:
				n1 = (next_row,next_col)
				n2 = (next_row,next_col+1)
			else:
				n1 = (next_row,next_col-1)
				n2 = (next_row,next_col)

			r1 = move(n1, step, WIDE_BOX[0])
			if r1 != n1:
				r2 = move(n2, step, WIDE_BOX[1])
				if r2 != n2:
					MAP[next_row][next_col] = who
					MAP[start[0]][start[1]] = FLOOR
					return (next_row, next_col)
				else:
					MAP[r1[0]][r1[1]] = FLOOR
					MAP[n1[0]][n1[1]] = WIDE_BOX[0]
					return start
			else:
				return start
	else:
		MAP[next_row][next_col] = who
		MAP[start[0]][start[1]] = FLOOR
		return (next_row, next_col)


def start_moving():
	_start =  START
	# for-loop because sys.setrecursionlimit() is L A M E
	for step in STEPS:
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
	print("Total score:", total) # 1490942, ????


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

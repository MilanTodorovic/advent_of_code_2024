# Advent of Code 2024 - Day 4
import re

XMAS = "XMAS"
MAX_ROWS = 0
MAX_COLUMNS = 0

def recombine(contents):
	global MAX_ROWS, MAX_COLUMNS
	
	revd = []
	up_down = []
	down_up = []
	diagonal_tl_br = []
	diagonal_br_tl = []
	diagonal_tr_bl = []
	diagonal_bl_tr = []
	
	# Right to left - reverse lines
	for c in contents:
		revd.append(c[::-1])

	# Up to down - rotate 90 degrees
	# len of a line
	for i in range(MAX_COLUMNS):
		tmp = []
		# amount of rows
		for j in range(MAX_ROWS):
			tmp.append(contents[j][i])
		up_down.append("".join(tmp))
			
	# Down to up - reverse the one above
	# I didn't reverse the order of the list before reversing the string cause it doesn't matter
	for c in up_down:
		down_up.append(c[::-1])

	# Diagonal top left to bottom right
	# len of a line
	for i in range(MAX_COLUMNS):
		if i == 0:
			# do all diagonals for this row
			for j in range(MAX_COLUMNS):
				tmp = []
				for k in range(MAX_ROWS):
					l = k+j
					if l < MAX_COLUMNS-1:
						tmp.append(contents[k][l])
					else:
						break
				diagonal_tl_br.append("".join(tmp))
		else:
			# do only one column per row
			tmp = []
			for j in range(i,MAX_ROWS):
				k = j-i
				if k < MAX_COLUMNS-i:
					tmp.append(contents[j][k])
				else:
					break
			diagonal_tl_br.append("".join(tmp))

	# Reverse the one above
	for c in diagonal_tl_br:
		diagonal_br_tl.append(c[::-1])

	# Diagonal top right to bottom left
	for i in range(MAX_ROWS):
		if i == 0:
			# do all diagonals for this row
			for j in range(MAX_COLUMNS-1,-1,-1):
				tmp = []
				for k in range(MAX_ROWS):
					l = j-k
					if l > -1:
						tmp.append(contents[k][l])
					else:
						break
				diagonal_tr_bl.append("".join(tmp))
		else:
			# do only one column per row
			tmp = []
			for j in range(i, MAX_ROWS):
				k = MAX_COLUMNS-j
				print(f"Row={j}, col={k}")
				if k < :
					tmp.append(contents[j][k])
				else:
					break
			print("".join(tmp))
			diagonal_tr_bl.append("".join(tmp))
	#print(diagonal_tr_bl)

	# Reverse the one above
	for c in diagonal_tr_bl:
		diagonal_bl_tr.append(c[::-1])

	return [revd, up_down, down_up, diagonal_tl_br, diagonal_br_tl, diagonal_tr_bl, diagonal_bl_tr]

def part_one():
	global XMAS, MAX_ROWS, MAX_COLUMNS
	amount = 0
	contenst = ""

	with open("./input.txt", "r") as file:
		contents = [c.strip() for c in file.readlines()] # remove '\n'

	MAX_ROWS = len(contents)
	MAX_COLUMNS = len(contents[0]) # assuming all rows of equal len

	a,b,c,d,e,f,g = recombine(contents)

	for c in contents:
		amount += len(re.findall(XMAS, c))
	for c in a:
		amount += len(re.findall(XMAS, c))
	for c in b:
		amount += len(re.findall(XMAS, c))
	for x in c:
		amount += len(re.findall(XMAS, x))
	for c in d:
		amount += len(re.findall(XMAS, c))
	for c in e:
		amount += len(re.findall(XMAS, c))
	for c in f:
		amount += len(re.findall(XMAS, c))

	print("Amount of 'XMAS' found:", amount) # 

def part_two():
	pass

if __name__ == "__main__":
	part_one()
	#part_two()
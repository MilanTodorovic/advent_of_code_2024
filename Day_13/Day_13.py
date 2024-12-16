# Advent of Code 2024 - Day 13 - DNF
# Solution which i don't understand:
#	b=(py*ax-px*ay)/(by*ax-bx*ay) a=(px-b*bx)/ax
import re
from collections import defaultdict


GAMES = defaultdict(list)
BUTTON_PATTERN = "\+(\d+)"
PRIZE_PATTERN = "=(\d+)"

def open_file():
	global GAMES

	i = 0
	with open("./test_input.txt", "r") as file:
		for line in file.readlines():
			if line != "\n":
				if line.find("A") > -1:
					_A = tuple(map(int, re.findall(BUTTON_PATTERN, line)))
					GAMES[i].append(_A)
				elif line.find("P") > -1:
					_P = tuple(map(int, re.findall(PRIZE_PATTERN, line)))
					GAMES[i].append(_P)
				else:
					_B = tuple(map(int, re.findall(BUTTON_PATTERN, line)))
					GAMES[i].append(_B)
			else:
				i += 1


def calculate(lst):
	_A = lst[0]
	_B = lst[1]
	_P = lst[2]
	goal = _P
	print("Game:")
	print(f"\tPx({_P[0]}) mod Ax({_A[0]}) {_P[0]%_A[0]}")
	print(f"\tPy({_P[1]}) mod Ay({_A[1]}) {_P[1]%_A[1]}")
	print(f"\tPx({_P[0]}) mod Bx({_B[0]}) {_P[0]%_B[0]}")
	print(f"\tPy({_P[1]}) mod By({_B[1]}) {_P[1]%_B[1]}")
	print("-----------------------------")

	if (_P[0] < _A[0] and _P[0] < _B[0]) or (_P[1] < _A[1] and _P[1] < _B[1]):
		# Prize is unreachable
		return (0,0)

	# Pressing the A button costs x3 coins
	#	if B*3 is moving a lot more, focus on pressing B
	if _B[0]*3 > _A[0]:
		_RB = _P[0]%_B[0], _P[1]%_B[1] 
		while True:
			# if there is a remained, subtrackt B from P and mod A
			if _RB[0] or _RB[1]:
				tmp = (_P[0]-_B[0], _P[1]-_B[1] )
				_RA = tmp[0]%_A[0], tmp[1]%_A[1]
				if _RA[0] or _RA[1]:
					print(_RB, _RA, tmp)
					continue
				else:
					# distance aka coins needed
					# from A to the reduces P
					# A = sqrt(pow((Px-Ax),2)+pow((Py-Ay),2))
					# from reduced P to real P
					# B = sqrt(pow((Px-P1x),2)+pow((Py-P1y),2))
					print(_RB, _RA, tmp)
					return (0,0)
	else:
		return (0,0)



def solve():
	open_file()
	for k, v in GAMES.items():
		r = calculate(v)
		print(f"Game {k+1} needs a total of {sum(r)} coins.")


if __name__ == "__main__":
	solve()

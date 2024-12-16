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
	print("Game:")
	print(f"\tPx({_P[0]}) mod Ax({_A[0]}) {_P[0]%_A[0]}")
	print(f"\tPy({_P[1]}) mod Ay({_A[1]}) {_P[1]%_A[1]}")
	print(f"\tPx({_P[0]}) mod Bx({_B[0]}) {_P[0]%_B[0]}")
	print(f"\tPy({_P[1]}) mod By({_B[1]}) {_P[1]%_B[1]}")
	print("-----------------------------")


def solve():
	open_file()
	for k,v in GAMES.items():
		calculate(v)


if __name__ == "__main__":
	solve()

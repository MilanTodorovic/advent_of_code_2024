# Advent of Code 2024 - Day 11
from copy import deepcopy # TOO SLOW!!!!
from time import time
from functools import cache
from collections import defaultdict

# This was all the magic. Tnx reddit
STONES = defaultdict(int)


@cache
def multiply_by_2024(number:int):
	return number*2024


@cache
def cut_stone(stone:str)->(int,int):
	half = len(stone)//2
	# removes leading zeroes
	return int(stone[:half]), int(stone[half:])


# this whole thing needs to use a dictionary to store occurances of numbers else the RAM is eaten up
# not my idea, ppl on reddit said so
def blink(times=1):
	global STONES
	# Rules:
	#	0 -> 1
	#	len("1000")%2 == 0 -> split into 2 stones int("10")|int("00") (no leading zeroes, so it becomes 0)
	#	none of the above - stone_nr * 2024
	# 	order is preserved! NOT! order doesn't matter!
	_t = time()
	for i in range(times):
		tmp = {k:v for k,v in STONES.items()}
		for stone, amount in tmp.items():
			if amount:
				if not stone: # k=0
					STONES[1] += amount
					# doing STONES[stone] = 0 doesn't work and I get the wrong answer
					STONES[stone] -= amount
				elif len(str(stone))%2 == 0:
					s1, s2 = cut_stone(str(stone))
					STONES[s1] += amount
					STONES[s2] += amount
					STONES[stone] -= amount
				else:
					STONES[multiply_by_2024(stone)] += amount
					STONES[stone] -= amount
		print(f"Blick {i+1} in {time()-_t:.2f} seconds.")
	print(f"Finished in {time()-_t:.2f} seconds.")
	_stones = 0
	for k,v in STONES.items():
		if v:
			_stones += v
	print(f"No. of stones:", _stones)


def open_file():
	content = None
	with open("./input.txt", "r") as file:
		content = file.readline().strip()
		content = [int(c.strip()) for c in content.split(" ")]
	return content


def solve(blink_times=1, part_two=False):
	global STONES

	content = open_file()
	print(content)
	# TODO: do the thing with dct look-ups
	# EDIT: I don't get why dicts are so much faster when doing these calculations.
	#	I am not going to steal anyone's solution for the sake of it.
	# EDIT 2: figured it out
	for c in content:
		STONES[c] += 1

	blink(blink_times)


if __name__ == "__main__":
	start = time()
	#solve(25) # 203457
	solve(75, True)
	end = time()
	print(f"Time took to compute: {end-start:.2f} seconds.")

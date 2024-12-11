# Advent of Code 2024 - Day 11
from copy import deepcopy
from time import time


def pre_calculate():
	# the first 5 steps
	pass

def blink(stones, times=1):
	# Rules:
	#	0 -> 1
	#	len("1000")%2 == 0 -> split into 2 stones int("10")|int("00") (no leading zeroes, so it becomes 0)
	#	none of the above - stone_nr * 2024
	# 	order is preserved!
	for i in range(times):
		_t = time()
		tmp = deepcopy(stones)
		split = 0
		for j, stone in zip(range(len(tmp)),tmp):
			if stone == "0":
				stones[j+split] = "1"
			elif len(stone)%2 == 0:
				half = len(stone)//2
				# removes leading zeroes
				s1, s2 = str(int(stone[:half])), str(int(stone[half:]))
				stones.pop(j+split)
				stones = stones[:j+split] + [s1,s2] + stones[j+split:]
				split += 1
			else:
				# pre-calculating the first 5 steps of every sub-10 number might be cheating
				# using @cache might be as well
				stones[j+split] = str(int(stone)*2024)
		print("Blick",i+1, "in", (time()-_t)%60, "seconds.")
	print(f"After {times} blinks:", stones)
	print(f"No. of stones after {times} blinks:", len(stones))


def open_file():
	content = None
	with open("./input.txt", "r") as file:
		content = file.readline().strip()
		content = [c.strip() for c in content.split(" ")]
	return content


def solve(blink_times=1, part_two=False):
	content = open_file()
	print(content)
	pre_calculate()
	# do the thing with dct look-ups
	blink(content, blink_times)


if __name__ == "__main__":
	start = time()
	solve(25)
	end = time()
	print("Time took to compute: ", (end-start)%60, " seconds.")
	#solve(25, True)
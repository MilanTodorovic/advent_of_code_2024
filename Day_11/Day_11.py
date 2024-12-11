# Advent of Code 2024 - Day 11
from copy import deepcopy # TOO SLOW!!!!
from time import time
from functools import cache
from multiprocessing import Process

@cache
def multiply_by_2024(number):
	return int(number)*2024


def pre_calculate():
	# the first 5 steps
	pass


def blink(stones, times=1):
	# Rules:
	#	0 -> 1
	#	len("1000")%2 == 0 -> split into 2 stones int("10")|int("00") (no leading zeroes, so it becomes 0)
	#	none of the above - stone_nr * 2024
	# 	order is preserved! NOT! order doesn't matter!
	_t = time()
	for i in range(times):
		#_t = time()
		tmp = [x for x in stones]
		# Deepcopy seems to be a lot slower then a list comprehension
		#tmp = deepcopy(stones)
		for j, stone in zip(range(len(tmp)),tmp):
			if stone == "0":
				stones[j] = "1"
			elif len(stone)%2 == 0:
				half = len(stone)//2
				# removes leading zeroes
				s1, s2 = stone[:half], str(int(stone[half:]))
				# Popping an element causes the whole list to shift, which takes precious time
				# 	Just mark it as skippable and deduct the number of skippable items from the total
				#stones.pop(j-popped)
				stones[j] = "i"
				stones.extend([s1,s2])
			else:
				if not stone == "i":
					# pre-calculating the first 5 steps of every sub-10 number might be cheating
					# using @cache might be as well
					stones[j] = str(multiply_by_2024(stone))

		print(f"Blick {i+1} in {time()-_t:.2f} seconds.")
		#print(f"\tNo. of stones:", len(stones))
	print(f"Finished in {time()-_t:.2f} seconds.")
	print(f"\tNo. of stones:", len(stones)-stones.count("i"))


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
	for i in range(len(content)):
		#p = Process(target=blink, args=[[content[i]], blink_times])
		#p.start()
		#p.join()
		blink([content[i]], blink_times)
	#blink(content, blink_times)


if __name__ == "__main__":
	start = time()
	#solve(25) # 203457
	solve(75, True)
	end = time()
	print(f"Time took to compute: {end-start:.2f} seconds.")
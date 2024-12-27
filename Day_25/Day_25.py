# Advent of Code 2024 - Day 25

from collections import defaultdict

FILE = ""
LOCKS = defaultdict(list)
KEYS = defaultdict(list)


def one_or_zero(character):
	return 1 if character == "#" else 0


def all_zero(iterable):
	# inverse all()
	for element in iterable:
		if element:
			return False
	return True


def open_file():
	global LOCKS, KEYS
	with open(FILE, "r") as file:
		i = 0
		check = True
		is_key =  False
		is_lock = False
		for line in file.readlines():
			if line != "\n":
				l = line.strip()
				masked = [one_or_zero(c) for c in l]

				if check:
					# we don't check if a key is valid by having all # in the last column
					is_lock = all(masked)
					is_key = all_zero(masked)
					check = False

				if is_lock:
					LOCKS[i].extend(masked)
				elif is_key:
					KEYS[i].extend(masked)
				else:
					# neither key nor lock
					continue
			else:
				i += 1
				check = True


def is_match(lock, key):
	for i in range(len(lock)):
		if not (lock[i] and key[i]):
			continue
		else:
			return False
	return True


def solve():
	macthes = 0
	for lock in LOCKS.values():
		for key in KEYS.values():
			if is_match(lock, key):
				macthes += 1
	print("Total matched keys and locks:", macthes) # 3365, 


if __name__ == "__main__":
	test =  False
	if test:
		FILE = "./test_input.txt"
	else:
		FILE = "./input.txt"
	open_file()
	solve()
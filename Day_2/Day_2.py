# Advent of Code 2024 - Day 2


def line_to_int_list(line):
	return [int(i) for i in line.split(" ")]


def retry(lst, i):
	# print(lst, i)
	if i < len(lst)-1:
		l1 = lst[::]
		l1.pop(i+1)
	else:
		l1 = [0,0]

	l2 = lst[::]
	l2.pop(i)

	if i > 0:
		l3 = lst[::]
		l3.pop(i-1)
	else:
		l3 = [0,0]

	# print(f"{l3} = {is_safe(l3)}, {l2} = {is_safe(l2)}, {l1} = {is_safe(l1)}")
	return is_safe(l1) or is_safe(l2) or is_safe(l3)


def decreasing(lst, pop=False):
	# print("Start decreasing:", lst)
	for i in range(0, len(lst)-1): 
		if (lst[i] > lst[i+1]) and ((lst[i] - lst[i+1]) <= 3):
				continue
		else:
			if pop:
				return retry(lst, i)
			else:
				# print("False: ", lst)
				return False
	else:
		# print("True: ", lst)
		return True


def increasing(lst, pop=False):
	# print("Start inceasring: ", lst)
	for i in range(0, len(lst)-1):
		if (lst[i] < lst[i+1]) and ((lst[i+1] - lst[i]) <= 3):
			continue
		else:
			if pop:
				return retry(lst, i)
			else:
				# print("False: ", lst)
				return False
	else:
		# print("True: ", lst)
		return True


def is_safe(lst):
	if lst[0] > lst[1]:
		return decreasing(lst)
	elif lst[0] < lst[1]:
		return increasing(lst)
	else:
		return False


def is_safer(lst, popped=False):
	if lst[0] > lst[1]:
		return decreasing(lst, True)
	elif lst[0] < lst[1]:
		return increasing(lst, True)
	else:
		if not popped:
			print(f"Popping 1st element of: {lst}")
			lst.pop(0)
			return is_safe(lst)
		else:
			# print("Popping first item didn't help. Returning False.")
			return False


def part_one():
	safe = 0
	with open("input.txt", "r") as file:
		for line in file.readlines():
			x = is_safe(line_to_int_list(line))
			if x:
				safe += 1
	print(safe) # 606


def part_two():
	safe = 0
	with open("input.txt", "r") as file:
		for line in file.readlines():
			x = is_safer(line_to_int_list(line))
			if x:
				# print("Final true: ", line)
				safe += 1
			# else:
			#	print("Final false: ", line)
	print(safe) # 644


if __name__ == "__main__":
	# part_one()
	part_two()
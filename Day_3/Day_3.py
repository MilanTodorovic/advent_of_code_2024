# Advent of Code 2024 - Day 3
import re

def part_one():
	result = 0
	with open("./input.txt", "r") as file:
		contents = file.read()
		regex = re.compile("mul\(([0-9]{1,3})\,([0-9]{1,3})\)")
		res = re.findall(regex, contents)
		for mul in res:
			result += int(mul[0])*int(mul[1])
		print(result) # 173731097

def part_two():
	result = 0
	flag = True
	with open("./input.txt", "r") as file:
		contents = file.read()
		regex = re.compile("mul\(([0-9]{1,3})\,([0-9]{1,3})\)|(do\(\))|(don't\(\))")
		res = re.findall(regex, contents)
		for mul in res:
			print(mul)
			if "don't()" in mul:
				flag = False
			elif "do()" in mul:
				flag = True
			if flag and (mul[0] and mul[1]):
				result += int(mul[0])*int(mul[1])
		print(result) # 93729253

if __name__ == "__main__":
	# part_one()
	part_two()
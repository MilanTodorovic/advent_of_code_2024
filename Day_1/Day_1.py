# Advent of Code - Day 1 PASSED

def part_one():
    lst_a = []
    lst_b = []
    res = []
    with open("advent_of_code/scripts/Day_1/input.txt", "r") as file:
        for line in file.readlines():
            # print(line)
            a, b = line.split()
            lst_a.append(int(a))
            lst_b.append(int(b))
    lst_a.sort()
    lst_b.sort()
    for i, j in zip(lst_a, lst_b):
        res.append(abs(i-j))
    print(sum(res)) # 1590491

def part_two():
    lst_a = []
    lst_b = []
    res = []
    with open("advent_of_code/scripts/Day_1/input.txt", "r") as file:
        for line in file.readlines():
            # print(line)
            a, b = line.split()
            lst_a.append(int(a))
            lst_b.append(int(b))
    for i in lst_a:
        j = lst_b.count(i)
        res.append(i*j)
    print(sum(res)) # 22588371

if __name__ == "__main__":
    # part_one()
    part_two()
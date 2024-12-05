# Advent of Code 2024 -Day 5

def read_input():
    rules = []
    pages = []
    p = False # a newline indicates end of page ordering rules
    with open("./input.txt", "r") as file:
        contents = file.readlines()
        for c in contents:
            if c == "\n":
                p = True
                continue
            if not p:
                rules.append(list(map(int,c.strip().split("|"))))
            else:
                pages.append(list(map(int,c.strip().split(","))))
    return rules, pages

def part_one():
    lst = []
    good_pages = []
    bad_pages = []
    rules, pages = read_input()
    for page in pages:
        for rule in rules:
            a, b = rule
            if a in page and b in page:
                if not page.index(a) < page.index(b):
                    bad_pages.append(page)
                    break
        else:
            good_pages.append(page)
    for page in good_pages:
        lst.append(page[len(page)//2])
    print("Sum of middle pages:",sum(lst)) # 4578
    part_two(rules, bad_pages)

def part_two(rules, bad_pages):
    lst = []
    for page in bad_pages[::]:
        # do more passes
        for i in range(5):
            for rule in rules:
                a, b = rule
                if a in page and b in page:
                    a_i = page.index(a)
                    b_i = page.index(b)
                    if not a_i < b_i:
                        page[a_i], page[b_i] = page[b_i], page[a_i]

    for page in bad_pages:
        lst.append(page[len(page)//2])
    print("Sum of pages:",sum(lst)) # 6179


if __name__ == "__main__":
    part_one()

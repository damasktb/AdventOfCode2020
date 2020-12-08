import re

bags = {}
for rule in open("Day7.txt"):
	bag, contains = rule.strip().split(" bags contain ")
	bags[bag] = {}

	for contained in re.findall(r"(\d\s\w+\s\w+) bag", contains):
		bags[bag][" ".join(contained.split()[1:])] = int(contained.split()[0])

gold = ["shiny gold"]
changed = True

while changed:
	changed = False
	for bag, contains in bags.items():
		for known in gold:
			if known in contains.keys() and bag not in gold:
				gold.append(bag)
				changed = True

print len(gold) - 1

memo = {}
def total(bag):
	t = 1
	if bag in memo:
		return memo[bag]
	for contained, count in bags[bag].items():
		t += (count * total(contained))
	memo[bag] = t
	return t

print total("shiny gold")-1

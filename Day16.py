import itertools, re

rules, mine, nearby = open("Day16.txt").read().split("\n\n")

valid = {}
for rule in rules.split("\n"):
	name = re.match(r"(\w+\s*\w+)", rule).group(0)
	valid[name] = [n for ranges in re.findall(r"(\d+)\-(\d+)", rule) for n in range(int(ranges[0]), int(ranges[1])+1)]

invalid = 0
tickets = []
for ticket in nearby.split("\n")[1:]:
	errors = sum([int(n) for n in ticket.split(",") if int(n) not in set(itertools.chain.from_iterable(valid.values()))])
	if not errors:
		tickets.append([int(n) for n in ticket.split(",")])
	invalid += errors

print invalid

possible = {field: [name for name, ranges in valid.items() if all(v in ranges for v in zip(*tickets)[field])] for field in range(len(tickets[0]))}
certain = possible.copy()
taken = set()
while len(taken) != len(tickets[0]):
	for field, name in possible.items():
		if len(name) == 1:
			taken.add(name[0])
		else:
			for name in (t for t in taken if t in certain[field]):
				certain[field].remove(name)

total = 1
mine = mine.split("\n")[1].split(",")
for field, name in certain.items():
	total *= int(mine[field]) if name[0].startswith("departure") else 1

print total

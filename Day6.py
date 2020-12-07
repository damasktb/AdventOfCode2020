groups = [group.split("\n") for group in open("Day6.txt").read().split("\n\n")]

print sum(len(set([answer for person in group for answer in person])) for group in groups)
print sum([len(set.intersection(*[set(person) for person in group])) for group in groups])

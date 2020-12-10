import itertools
from operator import mul

adaptors = sorted([int(a) for a in open("Day10.txt")])
adaptors.append(max(adaptors) + 3)

def getSteps(adaptors, steps = [1]):
	steps.extend([j-i for i, j in zip(adaptors[:-1], adaptors[1:])])
	return steps

s = getSteps(adaptors)
print s.count(1) * s.count(3)

repeats = [list(n) for step, n in itertools.groupby(s) if step == 1]
permutations = [max(2**(len(chain)-1), 1) if len(chain) <= 3 else 2**(len(chain)-1)-1 for chain in repeats]

print reduce(mul, permutations)

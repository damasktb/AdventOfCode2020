import itertools

numbers = [int(n) for n in open("Day1.txt")]

for pair in itertools.combinations(numbers, 2):
	if sum(pair) == 2020:
		print pair[0] * pair[1]

for trio in itertools.combinations(numbers, 3):
	if sum(trio) == 2020:
		print trio[0] * trio[1] * trio[2]

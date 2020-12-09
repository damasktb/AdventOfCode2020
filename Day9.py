numbers = [int(n) for n in open("Day9.txt")]
twentyfive = [n for n in numbers[:25]]

def valid(find, numbers):
	for n in numbers:
		if (find-n) in numbers:
			return True
	return False

def firstInvalid(numbers):
	for i, n in enumerate(numbers):
		if i < len(twentyfive):
			continue
		if valid(n, twentyfive):
			twentyfive.pop(0)
			twentyfive.append(n)
		else:
			return n

invalid = firstInvalid(numbers)
print invalid

sequence = [numbers[i:i+j] for i in range(0, len(numbers)) for j in range(1, len(numbers)-i+1) if sum(numbers[i:i+j]) == invalid]
valid = [s for s in sequence if len(s) > 1][0]
print min(valid) + max(valid)

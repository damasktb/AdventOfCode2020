from copy import deepcopy

seats = [list(row.strip()) for row in open("Day11.txt")]

def adjacent(seats, i, j):
	directions = ((i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1))
	return [seats[i][j] for (i, j) in directions if i>=0 and i<len(seats) and j>=0 and j<len(seats[0])].count("#")

before = []
after = seats
while before != after:
	before = after
	after = deepcopy(before)
	for i in range(len(seats)):
		for j in range(len(seats[0])):
			if before[i][j] == "L" and adjacent(before, i, j) == 0:
				after[i][j] = "#"
			elif before[i][j] == "#" and adjacent(before, i, j) >= 4:
				after[i][j] = "L"

print sum([row.count("#") for row in after])

def inSight(seats, i, j):
	deltas = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
	sight = []
	for iStep, jStep in deltas:
		iNext = i + iStep
		jNext = j + jStep
		while 0 <= iNext < len(seats) and 0 <= jNext < len(seats[0]):
			if seats[iNext][jNext] != ".":
				sight.append(seats[iNext][jNext])
				break
			iNext += iStep
			jNext += jStep
	return sight.count("#")


before = []
after = seats
while before != after:
	before = after
	after = deepcopy(before)
	for i in range(len(seats)):
		for j in range(len(seats[0])):
			if before[i][j] == "L" and inSight(before, i, j) == 0:
				after[i][j] = "#"
			elif before[i][j] == "#" and inSight(before, i, j) >= 5:
				after[i][j] = "L"

print sum([row.count("#") for row in after])

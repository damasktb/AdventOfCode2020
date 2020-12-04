height = sum(1 for line in open("Day3.txt"))
width = len(open("Day3.txt").readline())
snow = [list(line)[:-1] for line in open("Day3.txt")]

def trees(right, down):
	trees = 0
	x = 0
	for y in range(0, height, down):
		if snow[y][x] == "#":
			trees += 1
		x = (x + right) % (width-1)
	return trees

print trees(3, 1)
print trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2)

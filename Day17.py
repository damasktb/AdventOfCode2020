from itertools import product

grid = [l.strip() for l in open("Day17.txt")]

def oneRound(universe, dimensions):
    next = set(universe)
    possible = [range(min(min(zip(*universe)[i]), 0)-1, max(max(zip(*universe)[i]), 0)+2) for i in range(dimensions)]
    for point in product(*[possible[i] for i in range(dimensions)]):
        s = sum(t in universe for t in product(*([point[i], point[i]-1, point[i]+1] for i in range(dimensions))) if any(t[j] != point[j] for j in range(dimensions)))
        if point in universe and s not in (2, 3):
            next.remove(point)
        elif s == 3:
            next.add(point)
    return next

def sixRounds(dimensions):
    universe = set((x, y) + (0,)*(dimensions-2) for x,row in enumerate(grid) for y,cell in enumerate(row) if cell=='#')
    for i in range(6):
        universe = oneRound(universe, dimensions)
    return len(universe)

print sixRounds(3)
print sixRounds(4)

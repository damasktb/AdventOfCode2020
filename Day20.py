import operator

def getColumn(tile, i):
	return ''.join((row[i] for row in tile))

def getEdges(tile):
	return (tile[0], tile[-1], getColumn(tile, 0), getColumn(tile, len(tile[0])-1))

tiles = {}
unique = {}
with open("Day20.txt") as t:
	for tile in t.read().split("\n\n"):
		tile = tile.strip().split("\n")
		name = int(tile[0][tile[0].index(" "):tile[0].index(":")])
		tiles[name] = tile[1:]
		for border in getEdges(tile[1:]):
			flipped = border[::-1]
			if border in unique:
				del unique[border]
			elif flipped in unique:
				del unique[flipped]
			else: 
				unique[border] = name

print reduce(operator.mul, set([edge for edge in unique.values() if unique.values().count(edge) == 2]), 1)

# Part 2? We don't know her

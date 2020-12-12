NORTH, EAST, SOUTH, WEST, LEFT, RIGHT, FORWARD = 'NESWLRF'
moves = [(m[:1], int(m[1:])) for m in open("Day12.txt")]

position = 0j
facing = 1j
for move, distance in moves:
    if move == RIGHT:
        facing *= 1j ** (distance/90)
    elif move == LEFT:
        facing *= (-1j) ** (distance/90)
    else:
	multiplier = 1j if move == EAST else -1j if move == WEST else -1 if move == SOUTH else 1 if move == NORTH else facing
	position += multiplier * distance

print(abs(position.real) + abs(position.imag))

position = 0j
waypoint = 1+10j
for move, distance in moves:
    if move == RIGHT:
    	waypoint *= 1j ** (distance/90)
    elif move == LEFT:
        waypoint *= (-1j) ** (distance/90)
    elif move == FORWARD:
    	position += waypoint * distance
    else:
	multiplier = 1j if move == EAST else -1j if move == WEST else -1 if move == SOUTH else 1
	waypoint += multiplier * distance

print(abs(position.real) + abs(position.imag))

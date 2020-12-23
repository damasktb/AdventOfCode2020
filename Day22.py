p1, p2 = ([int(card) for card in player.split("\n")[1:]] for player in open("Day22.txt").read().split("\n\n"))

def combat(p1, p2):
	while p1 and p2:
		a = p1.pop(0)
		b = p2.pop(0)
		p1.extend((a, b) if a > b else ())
		p2.extend((b, a) if a < b else ())
	return p1, p2

def recursive(p1, p2, seen = set()):
	while p1 and p2:
		if (tuple(p1), tuple(p2)) in seen:
			return p1, p2
		seen.add((tuple(p1), tuple(p2)))
		a = p1.pop(0)
		b = p2.pop(0)
		if len(p1) >= a and len(p2) >= b:
			subp1, subp2 = recursive(p1[:a], p2[:b])
			p1Win = len(subp1) > 0
		else:
			p1Win = a > b
		p1.extend((a, b) if p1Win else ())
		p2.extend((b, a) if not p1Win else ())
	return p1, p2


def game(mode, p1, p2):
	p1, p2 = mode(p1[:], p2[:])
	winner = p1 if p1 else p2
	return sum(card * (len(winner)-position) for position, card in enumerate(winner))

print game(combat, p1, p2)
print game(recursive, p1, p2)

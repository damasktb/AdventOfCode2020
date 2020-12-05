def getSeatId(ticket, split=7):
	rows = [i for i in xrange(128)]
	seats = [i for i in xrange(8)]
	for c in list(ticket)[:split]:
		rows = rows[:len(rows)/2] if c == "F" else rows[len(rows)/2:]
	for c in list(ticket)[split:]:
		seats = seats[:len(seats)/2] if c == "L" else seats[len(seats)/2:]
	return rows[0] * 8 + seats[0]

seats = sorted([getSeatId(ticket) for ticket in open("Day5.txt")])

print seats[-1]
print [seat for seat in xrange(seats[0], seats[-1]) if seat not in seats]

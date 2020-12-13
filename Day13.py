import operator

timestamp, buses = open("Day13.txt")
offsets = [i for i, bus in enumerate(buses.split(",")) if bus not in "x"]
buses = [int(bus) for bus in buses.split(",") if bus not in "x"]

waits = [(bus - (int(timestamp) % bus), bus) for bus in buses]
print min(waits)[0] * min(waits)[1]

timestamp = 0
matched = 1
while matched < len(buses):
  timestamp += reduce(operator.mul, (buses[:matched]), 1)
  matched += 1 if all(((timestamp + offset) % bus == 0 for offset, bus in zip(offsets, buses)[:matched+1])) else 0

print timestamp

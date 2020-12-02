import re

entries = []
for entry in open("Day2.txt"):
	entries.append(re.match(r"(?P<low>[0-9]+)-(?P<high>[0-9]+) (?P<letter>[a-zA-Z]): (?P<password>.*)", entry).groupdict())

print sum([1 for p in entries if int(p["low"]) <= p["password"].count(p["letter"]) <= int(p["high"])])

entries = []
for entry in open("Day2.txt"):
	entries.append(re.match(r"(?P<low>[0-9]+)-(?P<high>[0-9]+) (?P<letter>[a-zA-Z]): (?P<password>.*)", entry).groupdict())

print sum([1 for p in entries if (p["password"][int(p["low"])-1] == p["letter"]) ^ (p["password"][int(p["high"])-1] == p["letter"])])

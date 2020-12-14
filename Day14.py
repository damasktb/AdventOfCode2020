import re

programs = [p.strip().split("\n") for p in open("Day14.txt").read().split("mask = ")][1:]

def mask(bits, mask):
	return "".join([bit if mask[i] == "X" else mask[i] for i,bit in enumerate(bits)])

def maskAddress(bits, mask):
	addresses = [[]]
	for i, bit in enumerate(bits):
		addresses = [a+[v] for v in (("0", "1") if mask[i] == "X" else bit if mask[i] == "0" else "1") for a in addresses]
	return sorted([int("".join(address), 2) for address in addresses])

memory = {}
for program in programs:
	for instr in program[1:]:
		instr = re.match(r"mem\[(?P<addr>\d+)\] = (?P<val>\d+)", instr).groupdict()
		memory[instr["addr"]] = int(mask("{0:036b}".format(int(instr["val"])), program[0]), 2)

print sum(memory.values())

memory = {}
for program in programs:
	for instr in program[1:]:
		instr = re.match(r"mem\[(?P<addr>\d+)\] = (?P<val>\d+)", instr).groupdict()
		for address in maskAddress("{0:036b}".format(int(instr["addr"])), program[0]):
			memory[address] = int(instr["val"])

print sum(memory.values())

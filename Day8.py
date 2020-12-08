instructions = [[i[0], int(i[1])] for i in (instr.split() for instr in open("Day8.txt"))]

def terminates(instructions, next=0, acc=0):
	seen = set()
	while next not in seen:
		seen.add(next)
		opcode, arg = instructions[next]
		if opcode == "jmp":
			next += arg
		else:
			next += 1
		if opcode == "acc":
			acc += arg
		if next >= len(instructions):
			return (True, acc)
	return (False, acc)

print terminates(instructions)[1]

def fix(instructions):
	for i, (opcode, arg) in enumerate(instructions):
		if opcode == "jmp":
			instructions[i] = ["nop", arg]
		elif opcode == "nop":
			instructions[i] = ["jmp", arg]
		else:
			continue
		fixed, acc = terminates(instructions)
		if fixed:
			return acc
		instructions[i] = [opcode, arg]

print fix(instructions)

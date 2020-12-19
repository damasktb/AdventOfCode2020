import re

rules, tests = open("Day19.txt").read().split("\n\n")
rules = dict((rule.split(":")[0].strip(), rule.split(":")[1].strip()) for rule in rules.split("\n"))

def match(rule, maxDepth=14):
	if rules[rule][0].startswith('"'):
		return rules[rule][1]
	if maxDepth == 0:
		return ""
	options = ["".join(match(r, maxDepth-1) for r in option.split()) for option in rules[rule].split("|")]
	return "|".join(options).join(("(?:", ")"))
           
print len([t for t in tests.split() if re.match(re.compile(match('0') + "$"), t)])

rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"

print len([t for t in tests.split() if re.match(re.compile(match('0') + "$"), t)])

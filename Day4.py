import re
passports = [entry.replace("\n", " ") for entry in open("Day4.txt").read().split("\n\n")]

def present(passport):
	return all([field in passport for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]])

print sum([1 for p in passports if present(p)])

def valid(passport):
	try:
		m = re.search(r"byr:(?P<byr>\d{4})", passport).groupdict()
		if not (1920 <= int(m["byr"]) <= 2002):
			return False
		m = re.search(r"iyr:(?P<iyr>\d{4})", passport).groupdict()
		if not 2010 <= int(m["iyr"]) <= 2020:
			return False
		m = re.search(r"eyr:(?P<eyr>\d{4})", passport).groupdict()
		if not 2020 <= int(m["eyr"]) <= 2030:
			return False
		m = re.search(r"hgt:(?P<hgt>\d+)(?P<unit>(cm|in))", passport).groupdict()
		if m["unit"] == "cm" and not (150 <= int(m["hgt"]) <= 193):
			return False
		if m["unit"] == "in" and not (59 <= int(m["hgt"]) <= 76):
			return False
		m = re.search(r"hcl:#(?P<hcl>[0-9a-f]*)", passport).groupdict()
		if not len(m["hcl"]) == 6:
			return False
		m = re.search(r"ecl:(?P<ecl>(amb|blu|brn|gry|grn|hzl|oth))", passport).groupdict()
		if not m["ecl"]:
			return False
		m = re.search(r"pid:(?P<pid>\d*)", passport).groupdict()
		if not len(m["pid"]) == 9:
			return False
		return True
	except Exception:
		return False

print sum([1 for p in passports if valid(p)])

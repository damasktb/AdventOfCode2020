import collections

candidates = collections.defaultdict(list)
foods = []
for ingredients, allergens in [line.strip(")").split("(contains") for line in open("Day21.txt").read().split("\n")]:
	foods.append(set(ingredients.split()))
	for allergen in allergens.split(","):
		candidates[allergen.strip()].append(set(ingredients.split()))

allergens = {}
while allergens.keys() != candidates.keys():
	for allergen in (c for c in candidates.keys() if c not in allergens.keys()):
		candidate = set.intersection(*candidates[allergen]) - set(allergens.values())
		if len(candidate) == 1:
			allergens[allergen] = candidate.pop()

print sum(len(food - set(allergens.values())) for food in foods)
print ",".join([translation for allergen, translation in sorted(allergens.items())])

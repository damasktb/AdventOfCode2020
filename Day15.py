numbers = [int(n) for n in open("Day15.txt").read().split(",")]
data = dict((n,i+1) for i,n in enumerate(numbers[:-1]))

def nth(n, this, past):
    for i in range(len(past)+1, n):
        last = past.get(this, i)
        past[this] = i
        this = i - last
    return this

print nth(2020, numbers[-1], data.copy())
print nth(30000000, numbers[-1], data.copy())

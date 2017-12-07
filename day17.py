import itertools

total = 150
sizes = list(sorted(map(int, open('day17.txt').read().split()), reverse=True))
loops = [range(total // s + 1) for s in sizes]
ms = [total // s for s in sizes]
t = 1
for m in ms:
    t *= m
print(t)
ret = 0
for counts in itertools.product(*loops):
    w = sum(size * count for size, count in zip(sizes, counts))
    if w == 150:
        ret += 1
print(ret)

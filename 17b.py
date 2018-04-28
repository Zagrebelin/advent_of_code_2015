import itertools
from collections import Counter


def calculate(target_mass, masses):
    ret = 0
    ranges = [[0, 1] for _ in masses]
    counter = Counter()
    for counts in itertools.product(*ranges):
        this_mass = sum(count * mass for count, mass in zip(counts, masses))
        if target_mass == this_mass:
            container_numbers = sum(counts)
            counter.update([container_numbers])
    min_numbers = min(counter.keys())
    return counter[min_numbers]


data = list(map(int, open('17.txt', 'r').read().split()))
print(calculate(150, data, ))

import itertools


def calculate(target_mass, masses):
    ret = 0
    ranges = [[0, 1] for _ in masses]
    for counts in itertools.product(*ranges):
        this_mass = sum(count * mass for count, mass in zip(counts, masses))
        if target_mass == this_mass:
            ret += 1
    return ret


data = list(map(int, open('17.txt', 'r').read().split()))
print(calculate(150, data, ))

def process(count):
    houses = [0 for _ in range(count)]
    for elf in range(1, count):
        for house in range(elf, count, elf):
            houses[house] += elf * 10
    return houses[1:]


def part_a():
    lo = 500000
    hi = lo * 2
    while lo != hi:
        print(lo, hi)
        mid = (lo + hi) // 2
        x = process(mid)
        if any(l >= 36000000 for l in x):
            hi = mid
        else:
            lo = mid

def process_b(count):
    houses = [0 for _ in range(count)]
    for elf in range(1, count):
        house_count = 0
        for house in range(elf, count, elf):
            houses[house] += elf * 11
            house_count += 1
            if house_count == 50:
                break
    return houses[1:]



def part_b():
    lo = 500000
    hi = lo * 2
    while lo != hi:
        mid = (lo + hi) // 2
        x = process_b(mid)
        valid = any(l >= 36000000 for l in x)
        print(f'{lo} .. {hi} {mid}={valid}')
        if valid:
            hi = mid
        else:
            lo = mid


part_b()
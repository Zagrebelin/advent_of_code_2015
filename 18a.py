SIZE_X = 0
SIZE_Y = 0


def calculate_on_neighbours(field: set, cell):
    ret = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            neighbour_cell = (cell[0] + dx, cell[1] + dy)
            ret += int(neighbour_cell in field)
    return ret


def parse_input(s, stuck_corners=False) -> set:
    global SIZE_X
    global SIZE_Y

    lines = s.splitlines(keepends=False)
    ret = set()
    for line_idx, line in enumerate(lines):
        for cell_idx, cell in enumerate(line):
            if cell == '#':
                ret.add((line_idx, cell_idx))
    SIZE_X = len(lines)
    SIZE_Y = len(lines[0])
    if stuck_corners:
        ret.add((0, 0))
        ret.add((0, SIZE_Y - 1))
        ret.add((SIZE_X - 1, 0))
        ret.add((SIZE_X - 1, SIZE_Y - 1))

    return ret


def step_a(field: set) -> set:
    ret = set()
    for x in range(SIZE_X):
        for y in range(SIZE_Y):
            cell = (x, y)
            state = cell in field
            nei_count = calculate_on_neighbours(field, cell)
            if state:
                if nei_count in (2, 3):
                    new_state = True
                else:
                    new_state = False
            else:
                if nei_count == 3:
                    new_state = True
                else:
                    new_state = False
            if new_state:
                ret.add(cell)
    return ret


def step_b(field: set) -> set:
    ret = set()
    for x in range(SIZE_X):
        for y in range(SIZE_Y):
            cell = (x, y)
            state = cell in field
            nei_count = calculate_on_neighbours(field, cell)
            if state and nei_count in (2, 3):
                ret.add(cell)
            elif not state and nei_count == 3:
                ret.add(cell)

    ret.add((0, 0))
    ret.add((0, SIZE_Y - 1))
    ret.add((SIZE_X - 1, 0))
    ret.add((SIZE_X - 1, SIZE_Y - 1))
    return ret


def show_field(step_idx, field, trace, verbose):
    if not trace:
        return
    if step_idx:
        print(f'After {step_idx} steps:')
    else:
        print('Initial state:')
    if verbose:
        for x in range(SIZE_X):
            for y in range(SIZE_Y):
                print('#' if (x, y) in field else '.', end='')
            print()
        print()
    else:
        print(field, end='\n')


def action(filename, step_count, step_func, stuck_corners, trace=False, verbose=False):
    if verbose and not trace:
        raise ValueError('Verbose without trace')
    field = parse_input(open(filename).read(), stuck_corners=stuck_corners)

    show_field(0, field, trace, verbose)
    for step_idx in range(step_count):
        field = step_func(field)
        show_field(step_idx + 1, field, trace, verbose)
    return len(field)


assert action('18_test_a.txt', 4, step_a, stuck_corners=False) == 4
print('part a', action('18.txt', 100, step_a, stuck_corners=False))

assert action('18_test_b.txt', 5, step_b, stuck_corners=True) == 17
print('part b', action('18.txt', 100, step_b, stuck_corners=True))  # 865 .. 3000

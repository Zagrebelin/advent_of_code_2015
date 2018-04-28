from collections import defaultdict
import re


def read(filename):
    rules = defaultdict(list)
    molecula = ''
    for line in open(filename):
        line = line.strip()
        if not line: continue
        if '=>' in line:
            from_, to_ = line.replace('=>', '').split()
            rules[from_].append(to_)
        else:
            molecula = line
    return rules, molecula


def action(filename):
    rules, molecula = read(filename)
    ret = 0
    replacements = set()
    for from_, tos in rules.items():
        parts = [(m.start(), m.end()) for m in re.finditer(from_, molecula)]
        for to_ in tos:
            for begin, end in parts:
                new = molecula[:begin] + to_ + molecula[end:]
                replacements.add(new)
    return len(replacements)


assert action('19_test_a1.txt') == 4
assert action('19_test_a2.txt') == 7
print('Part A', action('19.txt'), 509)

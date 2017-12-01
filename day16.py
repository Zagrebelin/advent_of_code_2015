import re


class SuePartA:
    def __init__(self, idx, params):
        self.idx = idx
        self.params = {k: int(v) for k, v in params.items()}

    def __eq__(self, other):
        for name, value in other.params.items():
            self_value = self.params.get(name, None)
            if self_value is None:
                continue
            if value != self_value:
                return False
        return True

    @classmethod
    def from_line(cls, line):
        match = re.match('Sue (\d+): (.*)', line)
        idx, criterias = match.groups()
        criterias = dict(re.findall('(\w+): (\d+)', line))
        return cls(idx, criterias)


class SuePartB(SuePartA):
    def __init__(self, idx, params):
        super().__init__(idx, params)

    def __eq__(self, other):
        for name, value in other.params.items():
            self_value = self.params.get(name, None)
            if self_value is None:
                continue
            if name in ('cats', 'trees'):
                if value > self_value:
                    return False
            elif name in ('pomeranians', 'goldfish'):
                if value < self_value:
                    return False
            elif value != self_value:
                return False
        return True


SueClass = SuePartB

need = SueClass(-1, {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1, })

for line in open('day16.txt'):
    sue = SueClass.from_line(line)
    if sue == need:
        print(sue.idx)

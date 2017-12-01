import re

class Sue:
    def __init__(self, params):
        self.params = {k:int(v) for k, v in params.items()}

    def match(self, criteria):
        for name, value in criteria.items():
            self_value = self.params.get(name, None)
            if self_value is not None and value != self_value:
                return False
        return True

sues= {}
for line in open('day16.txt'):
    match = re.match('Sue (\d+): (.*)', line)
    idx, criterias = match.groups()
    criterias = dict(re.findall('(\w+): (\d+)', line))
    sues[idx] = Sue(criterias)

need = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for idx, sue in sues.items():
    if sue.match(need):
        print(idx)
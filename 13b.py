import itertools
import pprint

plan = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
plan = open('13.txt').read()
rela = {}
pers = set()
for line in plan.split('\n'):
    line = line.strip('.')
    a, _, action, cnt, *_, b = line.split()
    cnt = int(cnt)
    if action=='lose':
        cnt = -1 * cnt
    rela[(a,b)] = cnt
    pers.add(a)
    pers.add(b)
for p in pers:
    rela[(p, 'myself')] = 0
    rela[('myself', p)] = 0
pers.add('myself')
opt = 0
for order in itertools.permutations(pers):
    this = 0
    for x in range(len(pers)):
        a = order[x]
        if x==len(pers)-1:
            b = order[0]
        else:
            b = order[x+1]
        this += rela[(a,b)]+rela[(b,a)]
    opt = max((opt, this))
print(opt)    



# 376
# 618
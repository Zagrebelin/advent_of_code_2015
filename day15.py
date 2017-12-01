from collections import namedtuple

"""
Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
"""


# Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories'])
class Ingredient():
    def __init__(self, **props):
        self.props = list(props.values())


ins = [
    [5, -1, 0, 0, 5],
    [-1, 3, 0, 0, 1],
    [0, -1, 4, 0, 6],
    [-1, 0, 0, 2, 8],
]

PROP_COUNT = len(ins[0])
INS_COUNT = len(ins)

ret = 0
cnt = [0, 0, 0, 0]
for cnt[0] in range(101):
    for cnt[1] in range(101):
        if sum(cnt[:2])>100:
            continue
        for cnt[2] in range(101):
            if sum(cnt[:3]) > 100:
                continue
            cnt[3] = 100 - sum(cnt[:3])
            if cnt[3] < 0:
                continue
            total = 1
            total_cal = sum(c * i[PROP_COUNT-1] for c, i in zip(cnt, ins))
            if total_cal!=500:  # part b condition
                continue        # part b condition
            for prop_idx in range(PROP_COUNT-1):
                prop_total = sum(c * i[prop_idx] for c, i in zip(cnt, ins))
                prop_total = max(prop_total, 0)
                total = total * prop_total
            ret = max(total, ret)
print(ret)

170*50*72

# 13882464
# 5585580000
# 6211814400
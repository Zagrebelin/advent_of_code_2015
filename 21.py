from collections import namedtuple
from itertools import combinations, chain

import math

Pers = namedtuple('Pers', ['hp', 'damage', 'armor'])
Item = namedtuple('Item', ['price', 'damage', 'armor'])


def hit(hp: int, armor: int, damage: int) -> int:
    return hp - max(1, damage - armor)


def is_player_win(player: Pers, boss: Pers) -> bool:
    p_hp = player.hp
    b_hp = boss.hp
    while p_hp > 0 and b_hp > 0:
        b_hp = hit(b_hp, armor=boss.armor, damage=player.damage)
        if b_hp <= 0:
            return True
        p_hp = hit(p_hp, armor=player.armor, damage=boss.damage)
        if p_hp <= 0:
            return False


assert hit(100, damage=8, armor=3) == 95
assert hit(100, damage=8, armor=300) == 99
assert is_player_win(player=Pers(hp=8, damage=5, armor=5), boss=Pers(hp=12, damage=7, armor=2))

weapons = [
    Item(price=8, damage=4, armor=0),
    Item(price=10, damage=5, armor=0),
    Item(price=25, damage=6, armor=0),
    Item(price=40, damage=7, armor=0),
    Item(price=74, damage=8, armor=0),
]

armors = [
    Item(price=0, damage=0, armor=0),  # no armor at all
    Item(price=13, damage=0, armor=1),
    Item(price=31, damage=0, armor=2),
    Item(price=53, damage=0, armor=3),
    Item(price=75, damage=0, armor=4),
    Item(price=102, damage=0, armor=5),
]

rings = [
    Item(price=25, damage=1, armor=0),
    Item(price=50, damage=2, armor=0),
    Item(price=100, damage=3, armor=0),
    Item(price=20, damage=0, armor=1),
    Item(price=40, damage=0, armor=2),
    Item(price=80, damage=0, armor=3),
]

min_price = math.inf
max_price = 0
for rgs in chain([], combinations(rings, 1), combinations(rings, 2)):  # 0 1 или 2 кольца
    for armor in armors:  # какой-нибудь армор
        for weapon in weapons:  # какой-нибудь вепон
            price = sum(r.price for r in rgs) + armor.price + weapon.price
            player = Pers(
                hp=100,
                damage=sum(r.damage for r in rgs) + weapon.damage,
                armor=sum(r.armor for r in rgs) + armor.armor)
            boss = Pers(hp=109, damage=8, armor=2)
            if is_player_win(player, boss):
                min_price = min(price, min_price)
            else:
                max_price = max(price, max_price)
print('A:', min_price)
print('B:', max_price)

# * одно из 5 оружий                  5
# * одно из 6 арморов                 6
# * кольца - сочетания 0 из 6 или     1
#          - сочетания 1 из 6 или     6
#          - сочетания 2 из 6 или     15
#
#
#
# итого: 5*6*(1+6+15) = 660 вариантов

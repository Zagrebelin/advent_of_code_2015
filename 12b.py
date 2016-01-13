import re
import json
import pprint

def summ(x):
    if type(x) is int:
        return x
    if type(x) is list:
        return sum(map(summ, x))
    if type(x) is dict:
        if 'red' in x.values():
            return 0
        return summ(list(x.values()))
    if type(x) is str:
        return 0
    print(type(x))


def summ_j(s):
    return summ(json.loads(s))


print(summ_j("""[1,2,3]"""), 6)
print(summ_j("""[1,{"c":"red","b":2},3]"""), 4)
print(summ_j("""{"d":"red","e":[1,2,3,4],"f":5}"""), 0)
print(summ_j("""[1,"red",5]"""), 6)
data = json.loads(open('12.txt').read())
print(summ(data))


# 38885
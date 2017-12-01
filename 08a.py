import re

def calc_bytes(s):
    return len(s)

def calc_chars(s):
    e=eval(s)
    return len(e)

def show(s, e1, e2):
    a1 = calc_bytes(s)
    a2 = calc_chars(s)
    print("{e1}-{a1}, {e2}-{a2}".format(e1=e1, e2=e2, a1=a1, a2=a2))

bs = cs = 0
rc = 0
for line in open('08.txt', 'r'):
    line = line.strip()
    rc += len(line) - len(eval(line))
    #bs += calc_bytes(line)
    #cs += calc_chars(line)
print(rc)
print('e-a, e-a')
show(r'"\\zrs\\syur"',0,0)
show('""', 2, 0)
show('"abc"', 5, 3)
show(r'"aaa\"aaa"', 10, 7)
show(r'"\x27"', 6, 1)
print(r'\x[a-f0-9]{2}')

"""
1045

1641

1940
1342
"""
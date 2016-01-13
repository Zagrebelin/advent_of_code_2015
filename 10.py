import re

def x(m):
	match = m.group()
	return '%d%s' % (len(match), match[0])


def calc(s):
	return re.sub(r'(\d)\1*', x, s)

assert calc('1')=='11'
assert calc('11')=='21'
assert calc('21')=='1211'
assert calc('1211')=='111221'
assert calc('111221')=='312211'

s = '1113122113'
for _ in range(50):
	print('.', end='', flush=True)
	s = calc(s)

print()
print(len(s))
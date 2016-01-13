import re

data = open('12.txt').read()
ms =re.findall(r'[-\d]+\b', data)
ms = sum(map(int, ms))
print(ms)
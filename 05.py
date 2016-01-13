import re
from collections import Counter

forbiden = ('ab', 'cd', 'pq',  "xy")
def valid(s):
	r1 = re.findall(r'(..).*\1', s)
	r2 = re.findall(r'(.).\1', s)
	v1, v2 = r1!=[], r2!=[]
	return v1 and v2

rc=0
for line in open('5.txt'):
	if valid(line):
		rc+=1
print(rc)
print('%s True'%valid('qjhvhtzxzqqjkmpb'))
print('%s True'%valid('xxyxx'))
print('%s False'%valid('uurcxstgmygtbstg'))
print('%s False'%valid('ieodomkazucvgmuy'))
print('%s False'%valid('aaa'))
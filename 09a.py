import itertools

dst = {}
nodes = set()
for line in open('9.txt'):
	a, _, z, _, l = line.split()
	l = int(l)
	dst[(a,z)] = l
	dst[(z,a)] = l
	nodes.add(a)
	nodes.add(z)
dd=0
for route in itertools.permutations(nodes):
	d = 0
	for idx in range(0, len(route)-1):
		d+= dst[(route[idx], route[idx+1])]
	dd = max((dd, d))

print(dd)
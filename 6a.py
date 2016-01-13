import re
cmds = {
	'turn off': lambda x: False,
	'turn on': lambda x: True,
	'toggle': lambda x: not x,
}

orders = open('6.txt', 'r').read()

orders = re.findall(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", orders)
field = { (x,y):False for x in range(0,1000) for y in range(0,1000)}
for order in orders:
	print('.', end='', flush=True)
	cmd, x1, y1, x2, y2 = order
	x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
	action = cmds[cmd]
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			field[(x,y)] = action(field[(x,y)])
lamps = field.values()
ons = filter(lambda lamp:lamp, lamps)
print(len(list(ons)))
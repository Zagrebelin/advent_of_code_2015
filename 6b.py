import re
cmds = {
	'turn off': lambda x: max((x-1,0)),
	'turn on': lambda x: x+1,
	'toggle': lambda x: x+2,
}

orders = open('6.txt', 'r').read()
orders = re.findall(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", orders)

field = [[0 for x in range(1000)] for y in range(1000)]
for order in orders:
	print('.', end='', flush=True)
	cmd, x1, y1, x2, y2 = order
	x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
	action = cmds[cmd]
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			field[x][y] = action(field[x][y])

print(sum(field[x][y] for x in range(1000) for y in range(1000)))
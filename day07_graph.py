import day07

colors = {
    'NOT': 'blue',
    'LSHIFT': 'lightgreen',
    'RSHIFT': 'lightgreen',
    'AND': 'red',
    'OR': 'pink',
    'LET': 'black',
}
ops = list(map(day07.parse, open('07.txt').readlines()))  # type: list[day07.Operation]
out = open('day07.dot', 'w')
print('digraph day_7 {', file=out)
for op in ops:
    if op.opcode in ('LSHIFT', 'RSHIFT'):
        print(f'   "{op.args[0]}" -> "{op.result}";', file=out)
    else:
        for a in op.args:
            if type(a) is str or op.opcode == 'LET':
                print(f'   "{a}" -> "{op.result}" [color={colors[op.opcode]}];', file=out)

print('}', file=out)
def execute(cmds, a=0, b=0):
    eip = 0
    regs = {'a': a, 'b': b}
    while True:
        cmd = cmds[eip]
        opcode, *args = cmd.split()
        if opcode == 'hlf':
            reg = args[0]
            regs[reg] //= 2
            eip += 1
        elif opcode == 'tpl':
            reg = args[0]
            regs[reg] *= 3
            eip += 1
        elif opcode == 'inc':
            reg = args[0]
            regs[reg] += 1
            eip += 1
        elif opcode == 'jmp':
            offset = int(args[0])
            eip += offset
        elif opcode == 'jie':
            reg, offset = args[0].strip(','), int(args[1])
            if regs[reg] % 2 == 0:
                eip += offset
            else:
                eip += 1
        elif opcode == 'jio':
            reg, offset = args[0].strip(','), int(args[1])
            if regs[reg] == 1:
                eip += offset
            else:
                eip += 1
        if eip >= len(cmds):
            break
    return regs


regs = execute('''inc a
jio a, +2
tpl a
inc a'''.splitlines(keepends=False))
assert regs['a'] == 2

cmds = open('23.txt').read().splitlines(keepends=False)
print('A:', execute(cmds)['b'])
print('B:', execute(cmds, a=1)['b'])

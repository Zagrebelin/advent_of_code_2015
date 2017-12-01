import re
from collections import defaultdict, namedtuple, Counter
from pprint import pprint


class Operation:
    def __init__(self, args, opcode, result):
        self.result = result
        self.opcode = opcode
        self.args = args
        self.a, *_ = args
        self.executed = False

    def can_execute(self, wires):
        valid_a = type(self.a) is int or self.a in wires
        valid_b = type(self.b) is int or self.b in wires or len(self.args) == 1
        return not self.executed and valid_a and valid_b

    def execute(self, wires):
        # print(self)
        if self.result not in wires:
            a = self.a if type(self.a) is int else wires.get(self.a, None)
            b = self.b if type(self.b) is int else wires.get(self.b, None)

            if self.opcode == 'LET':
                ret = a
            elif self.opcode == 'LSHIFT':
                ret = a << b
            elif self.opcode == 'RSHIFT':
                ret = a >> b
            elif self.opcode == 'AND':
                ret = a & b
            elif self.opcode == 'OR':
                ret = a | b
            elif self.opcode == 'NOT':
                ret = ~a
            else:
                raise ValueError(self.opcode)
            wires[self.result] = ret & 0xffff
        self.executed = True

    @property
    def b(self):
        return self.args[1] if len(self.args) == 2 else None

    def __str__(self):
        return f'{self.a} {self.opcode} {self.b} -> {self.result}'


def str_to_int(s):
    try:
        return int(s)
    except ValueError:
        return s


def parse(s: str) -> Operation:
    """
    x -> y
    x AND y -> z
    x OR y -> z
    x LSHIFT y -> z
    x RSHIFT y -> z
    NOT x -> y
    :param s:
    :return:
    """
    left, result = s.split('->')
    left, result = left.strip(), result.strip()
    left = left.split()
    ret = None
    if len(left) == 1:
        ret = Operation(opcode='LET', args=[str_to_int(left[0])], result=result)
    elif len(left) == 2 and left[0] == 'NOT':
        ret = Operation(opcode='NOT', args=[left[1]], result=result)
    elif len(left) == 3 and left[1] in ('AND', 'OR', 'LSHIFT', 'RSHIFT'):
        ret = Operation(opcode=left[1], args=[str_to_int(left[0]), str_to_int(left[2])], result=result)
    else:
        raise ValueError(f'{s} is invalid instruction')

    return ret


def execute(ops, wires):
    while not all(op.executed for op in ops):
        for op in ops:
            if op.can_execute(wires):
                op.execute(wires)


ops = list(map(parse, open('07.txt').readlines()))  # type: list[Operation]
wires = dict()

execute(ops, wires)
print('a: ', wires['a'])

wires2 = {'b': wires['a']}
for op in ops:
    op.executed = False
execute(ops, wires2)
print('b: ', wires2['a'])

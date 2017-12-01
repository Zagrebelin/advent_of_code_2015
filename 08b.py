def parse(s):
    ret = ''
    for c in s:
        if c == '"':
            ret += '\\"'
        elif c == '\\':
            ret += '\\\\'
        else:
            ret += c
    return f'"{ret}"'


assert len(parse(r'""')) == 6
assert len(parse(r'"abc"')) == 9
assert len(parse(r'"abc\"abc"')) == 16
assert len(parse(r'"\x27"')) == 11

s = 0
for line in open('08.txt'):
    line = line.strip()
    s += len(parse(line)) - len(line)
print(s)

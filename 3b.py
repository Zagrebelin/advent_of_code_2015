cmds = {
    '>': lambda p: (p[0]+1, p[1]),
    '<': lambda p: (p[0]-1, p[1]),
    '^': lambda p: (p[0], p[1]-1),
    'v': lambda p: (p[0], p[1]+1),
}

def solve(steps):
    visited = set()
    p1 = (0,0)
    p2 = (0,0)
    visited.add(p1)
    visited.add(p2)
    santa = True
    for step in steps:
        if santa:
            p1 = cmds[step](p1)
        else:
            p2 = cmds[step](p2)
        visited.add(p1)
        visited.add(p2)
        santa = not santa
    return len(visited)

#print('%d 3'%solve('^v'))
#print('%d 3'%solve('^>v<'))
#print('%d 11'%solve('^v^v^v^v^v'))
print(solve(open('3.txt').read()))
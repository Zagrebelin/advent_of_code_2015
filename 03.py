def solve(steps):
 visited = set()
 x=y=0
 visited.add((x,y))
 for step in steps:
  if step=='>': x+=1
  elif step=='<': x-=1
  elif step=='^': y-=1
  elif step=='v': y+=1
  else: print(step)
  visited.add((x,y))
 return len(visited)

print(solve(open('3.txt').read()))
rc = 0
for line in open('2.txt'):
   x,y,z = map(int, line.split('x'))
   s1 = x*y*z
   s2 = min((x+y+x+y, x+z+x+z, y+z+y+z))
   s=s1+s2
   rc += s
print(rc)

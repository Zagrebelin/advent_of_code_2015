rc = 0
for line in open('2.txt'):
   x,y,z = map(int, line.split('x'))
   s1 = 2*x*y + 2*x*z + 2*y*z
   s2 = min((x*y, x*z, y*z))
   s=s1+s2
   rc += s
print(rc)

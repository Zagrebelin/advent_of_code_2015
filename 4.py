from hashlib import md5

def calc(key, x):
  s = key+str(x)
  s = s.encode('latin-1')
  answer = md5(s).hexdigest()
  return all((x=='0' for x in answer[0:5]))

x = 1
key = 'ckczppom'
while not calc(key, x):
 x+=1
 if x % 1000==0:
  print(x)
print(x)

floor = 0
cnt=1
for s in open('1.txt', 'r', encoding='latin-1').read():
	if s=='(':
		floor+=1
	if s==')':
		floor-=1
	if floor==-1:
		break
	cnt+=1
print(cnt)
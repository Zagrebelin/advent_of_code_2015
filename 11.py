import re

thrs = 'abc bcd cde def efg fgh ghi hij ijk jkl klm lmn mno nop opq pqr qrs rst stu tuv uvw vwx wxy xyz'.split()
alfa = dec2alfa = 'abcdefghijklmnopqrstuvwxyz'
alfa2dec = {c:dec2alfa.find(c) for c in dec2alfa}


def valid(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    c1 = any((thr in password for thr in thrs))
    c2 = len(re.findall("(.)\\1+", password))>=2
    return c1 and c2

def pwd2dec(password):
    rc = 0
    for x in range(len(password)):
        c = password[-1*(x+1)] 
        d = alfa2dec[c]*(len(alfa)**x)
        rc += d
    return rc

def dec2pwd(password):
    rc = ''

    while password>0:
        c = password%26
        rc=dec2alfa[c]+rc
        password = password//26
    rc= 'a'*(8-len(rc))+rc
    return rc

def next_password(password):
    cnt = 0
    while True:
        cnt+=1
        if cnt%1000==0:
            print('.', end='', flush=True)
        password = dec2pwd(pwd2dec(password)+1)
        if valid(password):
            break
        if password=='abcdffaa':
            print(":(")
            break
    return password

print('%s false'%valid('hijklmmn'))
print('%s false'%valid('abbceffg'))
print('%s false'%valid('abbcegjk'))
print('%s  true'%valid('abcdffaa'))
print('%s  true'%valid('ghjaabcc'))
print('%d 0' %  pwd2dec('aa'))
print('%d 25'%pwd2dec('az'))
print('%d 26'% pwd2dec('ba'))
print('%d 702'% pwd2dec('bba'))

print('%s aa' %  dec2pwd(0))
print('%s az' % dec2pwd(25))
print('%s ba' % dec2pwd(26))
print('%s bba' % dec2pwd(702))
print('%s abcdffaa'%next_password('abcdefgh'))
#print('%s ghjaabcc'%next_password('ghijklmn'))
print(next_password('vzbxxyzz'))

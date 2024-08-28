f=open('new1.txt','r')
v=c=u=l=0
data=f.read()
for i in data:
    if i.isalpha():
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
        if i in 'aeiouAEIOU':
            v+=1
        else:
            c+=1
print('vowels=',v)
print('consonants=',c)
print('uppercase=',u)
print('lowercase=',l)
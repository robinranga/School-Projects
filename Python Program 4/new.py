import pickle
d={}
f=open('Std_dts.dat','wb')
while True:
    r=int(input('Enter Roll NO.  : '))
    n=input('Enter Name  : ')
    d['Roll No']=r
    d['Name']=n
    pickle.dump(d,f)
    ch=input('Write More ? (Y/N)')
    if ch in 'Nn':
        break
f.close()
found=0
roll_no=int(input('Enter Roll no whose name you want to display : '))
f=open('Std_dts.dat','rb')
try:
    while True:
        rec=pickle.load(f)
        if rec['Roll No']==roll_no:
           print(rec['Name'])
           found=1
           break
except EOFError:        
    f.close()
if found==0:
    print('sorry no record found')
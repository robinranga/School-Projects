import pickle
f= open('student.dat','wb')
while True:
    r=int(input('Enter Roll NO :'))
    n=input('Enter Name :')
    m=int(input('Enter Marks : '))
    record=[r,n,m]
    pickle.dump(record,f)
    ch=input('Do you Want to Enter more? (Y/N)')
    if ch in 'Nn':
        break
f.close()
f=open('student.dat','rb')
try:
    while True:
        rec=pickle.load(f)
        print(rec)
except EOFError:
    f.close()
f=open('student.dat','rb+')
rollno=int(input('Enter roll no whose marks you want to update  : '))
try:
    while True:
        pos=f.tell()
        rec=pickle.load(f)
        if rec[0]==rollno:
            um=int(input('Enter Updated Marks : '))
            rec[2]=um
            f.seek(pos)
            pickle.dump(rec,f)
except EOFError:   
    f.close()
f=open('student.dat','rb')
try:
    while True:
        rec=pickle.load(f)
        print(rec)
except EOFError:
    f.close()
    
import csv
def write():  
    f=open('detail.csv','w')
    wo=csv.writer(f)
    wo.writerow(['User_ID','Password'])
    while True:
        u_id=input('Enter User ID : ')
        pswd=input('Enter Password : ')
        data=[u_id,pswd]
        wo.writerow(data)
        ch=input('Do you want to enter more? (Y/N)  ')
        if ch in 'Nn':
            break
    f.close()
def read():
    f=open('detail.csv','r')
    ro=csv.reader(f)
    for i in ro:
        print(i)
def search():
    f=open('detail.csv','r')
    found=0
    u=input('Enter user ID to search : ')
    ro=csv.reader(f)
    for i in ro:
        next(ro)
        if i[0]==u:
            print(i[1])
            found=1
    f.close()
    if found==0:
        print('Sorry Not Found')
write()
read()
search()
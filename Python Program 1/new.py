file = open('new555.txt', 'r') 
data = file.readlines() 
for i in data: 
    print(i.replace(" ", "$"))
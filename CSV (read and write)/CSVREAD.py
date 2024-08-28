import csv
rows=[]
f=open('new.csv','r')
csvreader=csv.reader(f)
header=next(csvreader)
for r in csvreader:
    rows.append(r)
print(header)
print(r)
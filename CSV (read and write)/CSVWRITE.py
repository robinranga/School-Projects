import csv
f=open('f.csv','w+')
wr=csv.writer(f)
wr.writerow(['RN','NAME','CLASS'])
wr.writerow(['1','NAME1','12'])
wr.writerow(['2','NAME2','11'])
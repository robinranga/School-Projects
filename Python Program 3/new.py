f=open('sampleOLD.txt','r')
data=f.readlines()
fn=open('sampleNEW.txt','w')
fo=open('sampleOLD.txt','w')
for line in data:
    if 'a' in line:
        fn.write(line)
    else:
        fo.write(line)
import sys

nlist = []
for i in range(5):
    nlist.append(int(input()))
    
print(int(sum(nlist)/len(nlist)))
nlist.sort()
print(nlist[2])
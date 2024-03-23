import sys
n = int(sys.stdin.readline())
nlist = []
for i in range(n):
    nlist.append(int(input()))
    
nlist.sort()

for i in nlist:
    print(i)
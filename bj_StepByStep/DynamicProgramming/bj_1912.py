import sys

n = int(input())

nlist = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, n):
    nlist[i] = max(nlist[i], nlist[i] + nlist[i-1])
    
print(max(nlist))
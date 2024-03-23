import sys 
n = int(input())

storages = list(map(int, sys.stdin.readline().strip()))

d = [0] * 100

d[0] = storages[0]
d[1] = max(storages[0], storages[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + storages[i])
    
print(d[n - 1])
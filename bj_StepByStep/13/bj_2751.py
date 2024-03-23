import sys
n = int(sys.stdin.readline())
nlist = []
count = [0] * (10001)
for i in range(n):
    input = int(sys.stdin.readline())
    count[input] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i)
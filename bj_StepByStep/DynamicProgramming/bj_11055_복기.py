import sys
input = sys.stdin.readline

n = int(input().strip())
nlist = list(map(int, input().strip().split()))
dp = [0] * n
dp[0] = nlist[0]
for i in range(n):
    for j in range(i):
        if nlist[i] > nlist[j]:
            dp[i] = max(dp[i], dp[j] + nlist[i])
        else: 
            dp[i] = max(dp[i], nlist[i])
            
print(max(dp))
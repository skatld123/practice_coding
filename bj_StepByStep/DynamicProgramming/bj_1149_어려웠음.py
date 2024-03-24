import sys
n = int(input())

dp = [[0]*3 for _ in range(n)] 

houses = []
for i in range(n):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    houses.append((r, g, b))
    
dp[0][0], dp[0][1], dp[0][2] = houses[0][0], houses[0][1], houses[0][2]

for i in range(n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + houses[i][2]
    
print(min(dp[n -1]))
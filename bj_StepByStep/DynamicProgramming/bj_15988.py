import sys
input = sys.stdin.readline

n = int(input())
# dp[1] = 1 # 1
# dp[2] = 2 # 1+1, 2
# dp[3] = 4 # 1+2, 1+1+1, 2+1, 3
dp = [0, 1, 2, 4]
# 4부터는 3+1, 2+2, 1+3으로 볼 수 있음
# 5는 1+4, 2+3, 3+2, 4+1
for _ in range(n):
    num = int(input())
    for i in range(len(dp), num + 1):
        dp.append((dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009)
    print(dp[num])
import sys
input = sys.stdin.readline
# 포도주 잔의 개수
n = int(input().strip())
wines = [0]

dp = [0] * (n+1)
for _ in range(n):
    wines.append(int(input().strip()))
# 연속 3잔이 안된다는 것이 필요
# 3잔 연속을 제외할수있는 경우의 수: 
# 1. 현재잔 건너뛰기
# 2. 현재잔, i-1잔, i-3잔 먹기
# 3. 현재잔, i-2잔
dp[1] = wines[1]
if n > 1:
    dp[2] = wines[1] + wines[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], wines[i] + dp[i-2], wines[i] + wines[i-1] + dp[i -3])

print(dp[n])
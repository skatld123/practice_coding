n = int(input())

dp = [0] * (91)
# 1의 자리서부터 경우의 수 계산
dp[1] = 1
dp[2] = 1 # 10
dp[3] = 2 # 101, 100
#dp[4] = 3 1010, 1001, 1000
#dp[5] = 5 10101, 10100, 10010, 10001, 10000
if n > 3:
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
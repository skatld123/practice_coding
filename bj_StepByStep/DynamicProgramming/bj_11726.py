# 2 X a의 직사각형
a = int(input())
# 직사각형 길이만큼
dp = [0] * 1001

dp[1] = 1
dp[2] = 2
# a_i = 1 x a_(i-1) + a_(i-2)
if a > 2:
    for i in range(3, a + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[a])

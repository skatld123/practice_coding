def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    if n == 1:
        dp[1] = 1
    elif n == 2:
        dp[1] = 1
        dp[2] = 2  # 1-세로 2개 2-가로 2개
    else:
        dp[1] = 1
        dp[2] = 2  # 1-세로 2개 2-가로 2개
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]

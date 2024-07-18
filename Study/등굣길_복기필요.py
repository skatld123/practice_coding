def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(len(dp)):
        if not (i, 0) in puddles:
            dp[i][0] = 1
        else:
            break

    for i in range(len(dp[0])):
        if not (0, i) in puddles:
            dp[0][i] = 1
        else:
            break

    for x, y in puddles:
        dp[x - 1][y - 1] = -1

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] == 0 and i - 1 >= 0 and j - 1 >= 0:
                if dp[i - 1][j] == -1:
                    dp[i][j] = dp[i][j - 1]
                elif dp[i][j - 1] == -1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]

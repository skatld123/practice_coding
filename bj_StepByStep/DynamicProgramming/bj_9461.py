import sys

t = int(input())
answer = []
for i in range(t):
    n = int(input())

    # 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for j in range(4, n + 1):
        dp[j] = dp[j-2] + dp[j-3]
    
    answer.append(dp[n])

for i in answer:
    print(i)
    
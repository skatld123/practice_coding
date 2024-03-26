n = int(input())

steps = [0]
for i in range(n):
    steps.append(int(input()))

if  n == 1 :
    print(steps[1])
else:
    dp = [0] * (n + 1)
    dp[1] = steps[1]
    dp[2] = steps[2] + steps[1]
    for i in range(3, n + 1):
        # dp와 step을 잘 구분할 것
        dp[i] = max(steps[i-1] + dp[i-3],  dp[i-2]) + steps[i]

    print(dp[n])

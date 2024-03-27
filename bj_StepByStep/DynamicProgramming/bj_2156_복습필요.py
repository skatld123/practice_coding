n = int(input())

drinks = [0]
dp = [0] * (n + 1)
for i in range(n):
    drinks.append(int(input()))

dp[1] = drinks[1]
if n > 1:
    dp[2] = drinks[1] + drinks[2]
    for i in range(3, n + 1):
        dp[i] = max(drinks[i - 1] + dp[i - 3] + drinks[i], dp[i - 2] + drinks[i], dp[i-1]) 

print(dp[n])
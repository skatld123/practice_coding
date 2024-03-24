n = int(input())

dp = [0] * 1000001
# 1
dp[1] = 1
# 00, 11
dp[2] = 2
# 001, 100, 111
# dp[3] = 3
# 0011, 1001, 1111, 0000, 1100 
# dp[4] = 5 

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    
print(dp[n])
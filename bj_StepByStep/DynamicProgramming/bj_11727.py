import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0] * (n + 1)
dp[1] = 1
if n > 1:
    dp[2] = 3
    if n > 2:
        # 1부터 생각할 것이 아니라 뒤에서부터(i-1)부터 생각해볼 것
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + 2 * dp[i-2] 
    
print(dp[n] % 10007)
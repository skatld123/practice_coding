import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = []
for _ in range(n):
    numbers.append(int(input().strip()))

for num in numbers:
    dp = [0] * (num + 1)
    dp[1] = 1
    if num > 1: dp[2] = 2
    if num > 2: dp[3] = 4 # 1+1+1, 1+2, 2+1, 3
    if num > 3:
        # 4 이후부터는 1+3, 2+2, 3+1 인데, 
        for i in range(4, num + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[num])
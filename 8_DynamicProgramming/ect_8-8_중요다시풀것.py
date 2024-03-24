import sys

n, m = map(int, sys.stdin.readline().strip().split())

dp = [10001] * (m + 1)
dp[0] = 0
coins = []
for i in range(n):
    value = int(input())
    coins.append(value)

# 각 코인을 한개씩 사용하며 업데이트를 실행함
for i in range(n):
    # 해당 코인으로 목표 화폐단위 m까지의 반복문을 돌며 최소 개수를 측정
    for j in range(coins[i], m + 1):
        # 전단계가 방법이 있는 경우?
        if dp[j - coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
            
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

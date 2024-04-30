import sys
input = sys.stdin.readline

n = int(input().strip())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().strip().split())))

dp = [0] * (n + 1)
# 순서대로 상담을 하다가, 드는 비용을 dp에 저장
# 일자 이후의 일정을 더해주는 방식으로 고고
# 당일도 치는거임
for i in range(n-1, -1, -1):
    days, cost = nlist[i]
    if i + days <= n:
        dp[i] = max(cost + dp[i + days], dp[i+1])
    else:
        dp[i] = dp[i + 1]
    
print(dp[0])
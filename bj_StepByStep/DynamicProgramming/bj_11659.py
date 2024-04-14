import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

nlist = list(map(int, input().strip().split()))

rlist = []
for _ in range(m):
    a, b = map(int, input().strip().split())
    rlist.append((a, b))

dp = [0] * (n)
# 누적합을 구한 다음에 a 전의 누적 합을 빼면됌
dp[0] = nlist[0]
for i in range(1, len(nlist)):
    dp[i] = nlist[i] + dp[i-1]
dp = [0] + dp

for a, b in rlist:
    result = dp[b] - dp[a - 1]
    if a == b: print(nlist[a - 1])
    else : print(result)
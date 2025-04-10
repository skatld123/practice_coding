# 지름길 개수, 고속도로 길이
n, d = map(int, input().strip().split())
# 운전 최솟값 구할 것

load = []
for _ in range(n):
    # 시작 위치, 도착 위치, 지름길 길이
    load.append(list(map(int, input().strip().split())))

dp = [0] * (d + 1)
for i in range(1, len(dp)):
    dp[i] = i

for i in range(1, len(dp)):
    dp[i] = min(dp[i - 1] + 1, dp[i])
    for j in range(len(load)):
        start, arrive, length = load[j]
        if arrive <= d:
            dp[arrive] = min(dp[arrive], dp[start] + length)

print(dp[d])

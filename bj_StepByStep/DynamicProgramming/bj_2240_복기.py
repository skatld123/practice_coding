# 목표 : 받을 수 있는 자두 개수
# 조건 : 
# 1. 초마다 2개의 나무 중 하나에서 열매가 떨어짐
# 2. 열매가 떨어질 때, 그 나무 아래 있어야 함
# 3. 1초보다 짧은 시간에 다른 나무로 이동할 수 있음
# 4. 체력 제한이 있음

# T초 동안 자두가 떨어짐
# 최대 W만큼 움직일 수 있음
# 자두는 1번 나무 아래 있음
import sys
input = sys.stdin.readline

t, w = map(int, input().strip().split())
drops = [0]
for _ in range(t):
    drops.append(int(input().strip()))

# dp[매초][이동횟수] 
dp = [[0] * (w + 1) for _ in range(t + 1)]

# 1번에서 시작했기 때문에, 만약 w가 홀수라면 2번나무
# 짝수라면 1번 나무라는 뜻임
for i in range(1, t + 1):
    # 안움직이는 경우, 2가지의 경우의 수
    if drops[i] == 1: # 1번 나무라면
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    # 움직이는 경우
    for j in range(1, w + 1):
        if drops[i] == 2 and j % 2 == 1:
            # 움직여서 받아먹은 것과, 안움직이고 받아먹은 것
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif drops[i] == 1 and j % 2 == 0:
            # 움직여서 받아먹은 것과, 안움직이고 받아먹은 것
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            # 못 받아 먹었을 경우(움직여서 못먹은것과 가만히 있다가 못먹은 것)
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[t]))
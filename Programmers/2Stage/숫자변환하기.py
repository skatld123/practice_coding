from collections import deque


def solution(x, y, n):
    dp = [int(1e8)] * (y + 1)
    queue = deque([])
    queue.append(y)
    dp[y] = 0
    while queue:
        qidx = queue.popleft()
        if qidx == x:
            break
        if qidx - n >= 1:
            dp[qidx - n] = min(dp[qidx] + 1, dp[qidx - n])
            queue.append(qidx - n)
        else:
            continue
        if qidx % 2 == 0:
            dp[qidx // 2] = min(dp[qidx] + 1, dp[qidx // 2])
            queue.append(qidx // 2)
        if qidx % 3 == 0:
            dp[qidx // 3] = min(dp[qidx] + 1, dp[qidx // 3])
            queue.append(qidx // 3)

    return dp[x] if dp[x] != int(1e8) else -1

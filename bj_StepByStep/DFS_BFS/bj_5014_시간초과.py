import sys
from collections import deque

# f 건물 총 층, s 현재위치, g 스타트링크
f, s, g, u, d = map(int, sys.stdin.readline().strip().split())

visited = [0 for _ in range(f + 1)]
dp = [0 for _ in range(f + 1)]

def bfs():
    queue = deque([s])
    visited[s] = 1
    while queue:
        q = queue.popleft()
        if q == g:
            return dp[q]
        else:
            for next in (q - d, q + u):
                if 0 < next <= f and not visited[next]:
                    visited[next] = 1
                    dp[next] = dp[q] + 1
                    queue.append(next)
    return "use the stairs"

print(bfs())
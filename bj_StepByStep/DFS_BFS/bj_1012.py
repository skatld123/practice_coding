import sys
from collections import deque

def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    return 1

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    m, n, k = map(int, input().strip().split())
    graph = [[0] * m for _ in range(n)]
    for k_ in range(k):
        kx, ky = map(int, input().strip().split())
        graph[ky][kx] = 1
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                cnt += bfs(i, j)
    print(cnt)
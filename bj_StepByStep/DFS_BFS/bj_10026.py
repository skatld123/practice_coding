import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
graph_rg = []
for _ in range(n):
    graph.append(list(input().strip()))
visited = [[False] * n for _ in range(n)]


dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        qx, qy = queue.popleft()
        qcolor = graph[qx][qy]
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                gcolor = graph[nx][ny]
                if not visited[nx][ny] and qcolor == gcolor:
                    queue.append([nx, ny])
                    visited[nx][ny] = True

    return 1

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += bfs(i, j)
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += bfs(i, j)
print(cnt)
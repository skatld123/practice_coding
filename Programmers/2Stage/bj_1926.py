import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip().split())))

visited = [[False] * m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 1
    cnt = 1
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return 1, cnt

cnt = 0
maximum = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] != 0:
            c, area = bfs(i, j)
            cnt += c
            maximum = max(maximum, area) 

print(cnt)
print(maximum)
    
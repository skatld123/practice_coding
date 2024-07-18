import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = []

for i in range(n):
    graph.append(list(map(int, input().strip().split())))
visited = [[False] * n for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs_search(x, y, cnt):
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = True
    graph[x][y] = cnt
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    graph[nx][ny] = cnt

def bfs_birdge(num):
    queue = deque([])
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                queue.append([i, j])
                dist[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != num and graph[nx][ny] != 0:
                    return dist[x][y]
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    return
# 맵에 각 영역을 마킹
cnt = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs_search(i, j, cnt)
            cnt += 1
result = int(1e9)
for i in range(1, cnt):
    result = min(result, bfs_birdge(i))

print(result)
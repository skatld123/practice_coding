import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[qx][qy] + 1
                queue.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))
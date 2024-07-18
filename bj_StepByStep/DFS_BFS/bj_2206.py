import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))
    
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(len(visited))
print(len(visited[0]))
print(len(visited[0][0]))
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque([])
    queue.append([x, y, 0])
    visited[x][y][0] = 1
    while queue:
        qx, qy, punch = queue.popleft()
        if qx == (n - 1) and qy == (m - 1):
            return visited[qx][qy][punch]
        for i in range(4):
            nx, ny = dx[i] + qx, dy[i] + qy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and punch == 0:
                    queue.append([nx, ny, 1])
                    visited[nx][ny][1] = visited[qx][qy][0] + 1
                if graph[nx][ny] == 0 and not visited[nx][ny][punch]:
                    queue.append([nx, ny, punch])
                    visited[nx][ny][punch] = visited[qx][qy][punch] + 1
    return -1

print(bfs(0, 0))
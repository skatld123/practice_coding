import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
graph = []
for _ in range(n):
    line = list(map(int, list(input().strip())))
    graph.append(line)
    
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(x, y, z):
    queue = deque([[x, y, z]])
    visited[x][y][z] = 1
    while queue:
        qx, qy, cnt = queue.popleft()
        if qx == n - 1 and qy == m - 1:
            return visited[qx][qy][cnt]
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and cnt == 0:
                    queue.append([nx, ny, cnt + 1])
                    visited[nx][ny][1] = visited[qx][qy][0] + 1
                if graph[nx][ny] == 0 and not visited[nx][ny][cnt]:
                    queue.append([nx, ny, cnt])
                    visited[nx][ny][cnt] = visited[qx][qy][cnt] + 1
    return -1

print(bfs(0, 0, 0))
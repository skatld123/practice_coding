import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().strip().split())

graph = []
visited = [[[0] * (m) for _ in range(n)] for _ in range(h)]

for i in range(h):
    hlist = []
    for j in range(n):
        nlist = list(map(int, sys.stdin.readline().strip().split()))
        hlist.append(nlist)
    graph.append(hlist)

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

def bfs(starts_points):
    queue = deque()
    for sp in starts_points:
        queue.append(sp)
    day = 0
    while queue:
        qx, qy, qz = queue.popleft() # 위치
        if graph[qz][qy][qx] == 1:
            for i in range(6):
                nx, ny, nz = qx + dx[i], qy + dy[i], qz + dz[i]
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                    if graph[nz][ny][nx] == 0:
                        queue.append((nx, ny, nz))
                        graph[nz][ny][nx] = 1
                        visited[nz][ny][nx] = visited[qz][qy][qx] + 1
                        day = max(day, visited[nz][ny][nx])
    return day

isPerfect = True
starts_point = []
for k in range(h):
    for j in range(n):
        for i in range(m):
            if graph[k][j][i] == 1: 
                starts_point.append([i,j,k])
            if graph[k][j][i] == 0:
                isPerfect = False

if isPerfect:
    print(0)
else:
    answer = bfs(starts_point)
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if graph[k][j][i] == 0:
                    answer = -1
                    break
    print(answer)

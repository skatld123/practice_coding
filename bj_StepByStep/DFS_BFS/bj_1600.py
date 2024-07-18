import sys
from collections import deque

input = sys.stdin.readline

k = int(input().strip())
w, h = map(int, input().strip().split())
graph = []
for i in range(h):
    graph.append(list(map(int, input().strip().split())))

dmx, dmy = [0, 0, -1, 1], [-1, 1, 0, 0]
dhx, dhy = [2, 2, 1, 1, -2, -2, -1, -1], [-1, 1, -2, 2, -1, 1, -2, 2]

visited = [[[-1] * w for _ in range(h)] for _ in range(k + 1)]

def bfs(x, y):
    queue = deque([[0, x, y]])
    visited[0][x][y] = 1
    while queue:
        use_horse, qx, qy = queue.popleft()
        if qx == w - 1 and qy == h - 1:
            return visited[use_horse][qx][qy] - 1
        for i in range(len(dmx)):
            nx, ny = qx + dmx[i], qy + dmy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != 1 and visited[use_horse][nx][ny] == -1:
                    visited[use_horse][nx][ny] = visited[use_horse][qx][qy] + 1
                    queue.append([use_horse, nx, ny])

        if use_horse < k:
            for i in range(len(dhx)):
                nx, ny = qx + dhx[i], qy + dhy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] != 1 and visited[use_horse][nx][ny] == -1:
                        visited[use_horse + 1][nx][ny] = visited[use_horse][qx][qy] + 1
                        queue.append([use_horse + 1, nx, ny])

    return -1

print(bfs(0, 0))
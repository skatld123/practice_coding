import sys
from collections import deque
input = sys.stdin.readline

def bfs_num(x, y, cnt):
    queue = deque([])
    queue.append([x, y])
    graph[x][y] = cnt
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    graph[nx][ny] = cnt

def bfs_bridge(num):
    queue = deque([])
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                dist[i][j] = 0
                queue.append([i, j])
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    dist[nx][ny] = dist[qx][qy] + 1
                if graph[nx][ny] != num and graph[nx][ny] != 0:
                    return dist[qx][qy]
    return
n = int(input().strip())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

# 섬에 숫자 달기
# 숫자 달고 0을 +1로 바꿔보기 
visited = [[False] * n for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

cnt = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs_num(i, j, cnt)
            cnt += 1
minimum = 2*n
for i in range(1, cnt):
    answer = min(minimum, bfs_bridge(i))
print(answer)
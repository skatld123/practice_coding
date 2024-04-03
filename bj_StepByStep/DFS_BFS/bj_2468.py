# 물이 차는 for문을 진행 n이 2가 최소니까 2부터 중가하는 반복문 
# 방문한 곳을 1로, 잠긴 곳을 2로 설정
# 방문한 곳은 냅두고 높이와 방문 안한곳을 기준으로 bfs를 하고 성공적으로 하면 1을 리턴
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = []
min_value = 100
max_value = 1
for i in range(n):
    line = list(map(int, input().strip().split()))
    min_value = min(min_value, min(line))
    max_value = max(max_value, max(line))
    graph.append(line)

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(w, x, y):
    queue = deque([[x, y]])
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > w and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    return 1

max_area = 1
for w in range(min_value, max_value + 1):
    cnt = 0
    visited = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > w and not visited[i][j]:
                cnt += bfs(w, i, j)
    max_area = max(max_area, cnt)

print(max_area)


import sys
from collections import deque
n = int(sys.stdin.readline().strip())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False]* n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    cnt = 0
    queue = deque([(x, y)])
    while queue:
        qx, qy = queue.popleft()
        if graph[qx][qy] == 1 and not visited[qx][qy]:
            visited[qx][qy] = True
            cnt += 1
            for i in range(4):
                nx, ny = qx + dx[i], qy + dy[i]
                if 0 <= nx < n and 0 <= ny < n: 
                    if graph[nx][ny] == 1 and visited[nx][ny] == False:
                        queue.append([nx, ny])
    return cnt

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
for num in sorted(answer):
    print(num)
# 문제를 똑바로 읽고 정답을 잘 유추하자. 같은 답이더라도 틀린 방식으로 유도되었을 수도 있음
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

# 1년마다 카운트
# 얼음이 녹으므로 주변의 0이 몇개인지 확인해야함
# 빙산이 다 녹으면 0
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

# 얼음녹이기
def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        qx, qy = queue.popleft()
        sea_cnt = 0
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    sea_cnt += 1
                else:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
        minus[qx][qy] = graph[qx][qy] - sea_cnt if (graph[qx][qy] - sea_cnt) > 0 else 0
    return 1

year = 0 
while True:
    areas = 0
    minus = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                areas += bfs(i, j)
    if areas == 0:
        print(0)
        break
    elif areas > 1:
        print(year)
        break
    else:
        graph = minus
        year += 1

# 1연쇄 -> 여러 그룹이 터져도 1연쇄
# 같은색 뿌여 4개 이상이면 펑
import sys
from collections import deque

input = sys.stdin.readline

graph = []
for _ in range(12):
    graph.append(list(input().strip()))
visited = [[False] * 6 for _ in range(12)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

# 덩어리 검사
def bfs(sx, sy):
    queue = deque([])
    queue.append([sx, sy]) # 시작지점, history
    visited[sx][sy] = True
    color = graph[sx][sy]
    history = [[sx, sy]]
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    history.append([nx, ny])
                    queue.append([nx, ny])
    history.sort(key=lambda x : (x[1], x[0])) # 한줄씩 땡겨야하므로, 열부터 순서차적으로, 그다음 행을 보자
    return history

# 터지고 나서 어떻게 내려오게 할까?
# 일단 Visited False로 다시 돌리고 재검사를 수행
# 그리고 . 으로 바꾸고 만약 자신의 아랫줄이 . 이면 땡겨서 내려오면 되겠네
chain = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    booms = []
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and graph[i][j] != "." and graph[i][j] != "*":
                history = bfs(i, j)
                if len(history) > 3:
                    for x, y in history:
                        graph[x][y] = "*"
                    booms += history
    
    if len(booms) == 0: 
        break
    # 폭탄 위치 가져올 수 있음
    for (bx, by) in booms:
        # 그 위에서만 땡겨오면 되지 않나
        for k in range(bx, 0, -1):
            graph[k][by] = graph[k-1][by]
        graph[0][by] = "."
    
    chain += 1

print(chain)

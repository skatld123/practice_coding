import sys
from collections import deque

def bfs(r, c, d):
    queue = deque([[r, c, d]])
    clean_cnt = 1
    cleaned[r][c] = True
    while queue:
        qx, qy, ro = queue.popleft()
        temp_ro = ro
        isMove = False
        for i in range(4):
            ro = ro - 1 if ro - 1 >= 0 else 3
            nx, ny = qx + dx[ro], qy + dy[ro]
            # 청소되지 않은 빈칸이 있는 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if not cleaned[nx][ny]:
                    queue.append([nx, ny, ro])
                    cleaned[nx][ny] = True
                    clean_cnt += 1
                    isMove = True
                    break
        if not isMove:
            nr = temp_ro - 2 if temp_ro - 2 >= 0 else 2 + temp_ro #후진 방향
            nx, ny = qx + dx[nr], qy + dy[nr]
            if graph[nx][ny] == 0 and 0 <= nx < n and 0 <= ny < m:
                queue.append([nx, ny, temp_ro]) # 정면을 바라보고 후진
                if not cleaned[nx][ny]: 
                    cleaned[nx][ny] = True
                    clean_cnt += 1
            else:
                return clean_cnt
    return clean_cnt

input = sys.stdin.readline
n, m = map(int, input().strip().split())
r, c, d = map(int, input().strip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

cleaned = [[False] * m for _ in range(n)]

# 북, 동, 남, 서
rotate = [0, 1, 2, 3]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

print(bfs(r, c, d))



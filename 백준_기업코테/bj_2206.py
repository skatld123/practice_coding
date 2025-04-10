from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())

mapp = [list(map(int, input().strip())) for _ in range(N)]

# 부수고 이동해도 되고 아니여도 됨

visited = [[[False] * 2 for i in range(M)] for _ in range(N)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs():
    queue = deque([])
    # 벽을 아직 안부셨으면 0, 부셨으면 1
    queue.append([0, 0, 0, 0])
    visited[0][0][0] = 0

    while queue:
        qx, qy, isBroken, cnt = queue.popleft()
        if qx == N - 1 and qy == M - 1:
            return cnt + 1

        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if mapp[nx][ny] == 0:
                    if not visited[nx][ny][isBroken]:
                        queue.append([nx, ny, isBroken, cnt + 1])
                        visited[nx][ny][isBroken] = True

                if mapp[nx][ny] == 1:
                    if isBroken == 0 and not visited[nx][ny][1]:
                        queue.append([nx, ny, 1, cnt + 1])
                        visited[nx][ny][1] = True
    return -1

print(bfs())

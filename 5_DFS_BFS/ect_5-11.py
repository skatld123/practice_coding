# 미로탈출
from collections import deque
n, m = map(int, input().split())

maze = []
for i in range(n) :
    maze.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1인 것을찾으면 된다. 1을 찾고 이동할 경우 해당 노드의 값에 + 1
def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if maze[nx][ny] == 0 :
                continue
            if maze[nx][ny] == 1 :
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n - 1][m - 1]

print(bfs(0, 0))
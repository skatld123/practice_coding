import sys
from collections import deque
input = sys.stdin.readline

while True:
    l, r, c = map(int, input().strip().split())
    if l == 0 and r == 0 and c == 0:
        break
    graph = []
    start_node = []
    finish_node = []
    for il in range(l):
        floor = []
        for ir in range(r):
            line = list(input().strip())
            if "S" in line:
                start_node = [ir, line.index("S"), il]
            if "E" in line:
                finish_node = [ir, line.index("E"), il]
            floor.append(line)
        blank = input().strip()
        graph.append(floor)

    visited = [[[0]* c for _ in range(r)] for _ in range(l)]
    dx, dy, dz = [0, 0, -1, 1, 0, 0], [-1, 1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 1]
    # dx - r , dy - c, dz - l
    def bfs(z, x, y):
        queue = deque([[z, x, y]])
        visited[z][x][y] = 1
        while queue:
            qz, qx, qy = queue.popleft()
            for i in range(6):
                nx, ny, nz = qx + dx[i], qy + dy[i], qz + dz[i]
                if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                    if graph[nz][nx][ny] != "#" and not visited[nz][nx][ny]:
                        queue.append([nz, nx, ny])
                        visited[nz][nx][ny] = visited[qz][qx][qy] + 1
                        
    sx, sy, sz = start_node
    bfs(sz, sx, sy)
    fx, fy, fz = finish_node
    if not visited[fz][fx][fy]:
        print("Trapped!")
    else:
        print(f'Escaped in {visited[fz][fx][fy] - 1} minute(s).')
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]
    
    for r in rectangle:
        lx, ly, rx, ry = map(lambda x: x*2, r)
        for i in range(lx, rx + 1):
            for j in range(ly, ry + 1):
                if lx < i < rx and ly < j < ry:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    
    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    queue = deque([[cx, cy]])
    visited[cx][cy] = True
    while queue:
        qx, qy = queue.popleft()
        if qx == ix and qy == iy:
            return visited[qx][qy] // 2
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[qx][qy] + 1
                
    return answer
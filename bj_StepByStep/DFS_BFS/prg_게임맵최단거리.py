from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y, fx, fy, visited, graph):
    queue = deque([[x, y]])
    visited[x][y] = True
    answers = []
    while queue:
        qx, qy = queue.popleft()
        if qx == fx and qy == fy:
            answers.append(graph[qx][qy])
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx <= fx and 0 <= ny <= fy:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[qx][qy] + 1
                        visited[nx][ny] = True
                        queue.append([nx, ny])
    if not answers:
        return -1
    else:
        return min(answers)
    
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [([False] * m) for _ in range(n)]
    answer = bfs(0, 0, n - 1, m - 1, visited, maps)
    return answer
from collections import deque


def solution(n, m, x, y, queries):
    answer = 0
    qdict = {0: (0, -1), 1: (0, 1), 2: (-1, 0), 3: (1, 0)}
    qlist = make_qlist(queries, qdict)
    for i in range(n):
        for j in range(m):
            queue = deque(qlist[:])
            answer += bfs(i, j, x, y, n, m, queue)
    return answer


def make_qlist(queries, qdict):
    qlist = []
    for dr, dx in queries:
        nx, ny = qdict[dr]
        for i in range(dx):
            qlist.append((nx, ny))
    return qlist


def bfs(sx, sy, fx, fy, n, m, queue):
    nx, ny = sx, sy
    while queue:
        qx, qy = queue.popleft()
        if 0 <= nx + qx < n and 0 <= ny + qy < m:
            nx, ny = nx + qx, ny + qy
        else:
            continue
    if nx == fx and ny == fy:
        return 1
    return 0

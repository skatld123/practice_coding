# import sys
# from collections import deque

# def bfs(x, y, count, visited):
#     queue = deque([[x, y]])
#     visited[x][y] = True
#     count += 1
#     while queue:
#         qx, qy = queue.popleft()
#         for i in range(4):
#             nx, ny = qx + dx[i], qy + dy[i]
#             if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 count += 1
#                 queue.append([nx, ny])
#     return count

# input = sys.stdin.readline

# h, w, n, m = map(int, input().rstrip().split())

# dx, dy = [-n - 1, n + 1, 0, 0], [0, 0, m + 1, -m - 1]

# cls_room = [[0] * w for _ in range(h)]

# maximum = 0

# for i in range(m + 1):
#     for j in range(n + 1):
#         maximum = max(bfs(i, j, 0, [[False] * w for _ in range(h)]), maximum)  # 세, 가

# print(maximum)


import math 
h, w, n, m = map(int, input())

a = math.ceil(w/(m + 1))
b = math.ceil(h/(n + 1))
answer = a * b
print(answer)

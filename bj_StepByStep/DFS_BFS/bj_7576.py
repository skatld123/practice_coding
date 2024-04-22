import sys
from collections import deque

m, n = map(int, input().strip().split())
graph = []
starts = []
for _ in range(n):
    nlist = list(map(int, input().strip().split()))
    for i in range(len(nlist)):
      if nlist[i] == 1:
        starts.append((_, i))
    graph.append(nlist)

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(starts):
    queue = deque([])
    for x, y in starts:
        queue.append((x, y))
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[qx][qy] + 1
    return 

isPerfect = True
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0: isPerfect=False
      
if not isPerfect:
  bfs(starts)
  
  maximum = 0
  for i in range(n):
      if 0 in graph[i]:
          maximum = -1
          break
      else:
          max_ = max(graph[i]) - 1
          maximum = max(maximum, max_)
  print(maximum)
else:
    print(0)
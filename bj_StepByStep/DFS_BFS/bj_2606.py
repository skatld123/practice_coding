import sys
from collections import deque
cp_cnt = int(input())
link_cnt = int(input())

graph = [[] for _ in range(cp_cnt + 1)]
visited = [False] * (cp_cnt + 1)
for i in range(link_cnt):
    snode, fnode = map(int, sys.stdin.readline().strip().split())
    if not fnode in graph[snode]: graph[snode].append(fnode)
    if not snode in graph[fnode]: graph[fnode].append(snode)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        nod = queue.popleft()
        for n in graph[nod]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
    return visited.count(True) - 1 # 1번 컴퓨터를 제외

print(bfs(1))
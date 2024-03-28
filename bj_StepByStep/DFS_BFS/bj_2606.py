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

print(graph)

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        nod = queue.popleft()
        for n in graph[nod]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True
    return visited.count(True)

visited[1] = True
print(bfs(1))
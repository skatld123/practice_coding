import sys
from collections import deque

n = int(input())

sp, fp = map(int, sys.stdin.readline().strip().split())

m = int(input())

graph = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
for i in range(m):
    sn, fn = list(map(int, sys.stdin.readline().strip().split()))
    if not fn in graph[sn]: graph[sn].append(fn)
    if not sn in graph[fn]: graph[fn].append(sn)

def bfs(start_node, finish_node):
    queue = deque()
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        
        if node == finish_node:
            return cnt[finish_node]
        for n in graph[node]:
            if cnt[n] == 0:
                queue.append(n)
                cnt[n] = cnt[node] + 1
    
    return -1

print(bfs(sp, fp))
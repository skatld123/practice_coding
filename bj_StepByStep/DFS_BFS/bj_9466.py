import sys
from collections import deque

input = sys.stdin.readline
t = int(input().strip())

# 서로를 가르켜야 함
def bfs(idx, student):
    # 4, 7, [4] -> 7, 6, [4,7] -> 6, 4, [4,7,6]
    # 1, 3, [1] -> 3, 3, [1, 3] -> 3
    # 2, 1, [2] -> 1, 3, [2, 1] -> 3, 3, [2, 1, 3]
    queue = deque([[idx, student, [idx]]])
    visited[idx] = True
    while queue:
        qi, qstu, qgrp = queue.popleft()
        if not visited[qstu]:
            visited[qstu] = True
            queue.append([qstu, nlist[qstu][1], qgrp + [qstu]])
        else:
            if qstu in qgrp:
                index = qgrp.index(qstu)
                return qgrp[index:]
            else: return False
        
for _ in range(t):
    n = int(input().strip())
    nlist = list(map(int, input().strip().split()))
    # [(1,3), (2,1), (3,3), ...]
    for idx, stu in enumerate(nlist):
        nlist[idx] = [idx + 1, stu]
    nlist = [[0, 0]] + nlist
    visited = [False] * (n + 1)
    
    groups = []
    for i in range(1, len(nlist)):
        if visited[nlist[i][0]]: continue
        group = bfs(nlist[i][0], nlist[i][1])
        if group:
            groups += group
    print(n - len(groups))
import sys
from collections import deque
# 수빈이 n, 동생 k
n, k = map(int, sys.stdin.readline().strip().split())
visited = [False] * 100001

def bfs(start):
    queue = deque([[start, 0, [start]]]) # 시작위치, 초, 경로 입력
    visited[start] = True
    # 만약 출발지가 앞이라면
    if start > k:
        return start - k, [int(x) for x in range(n, k - 1, -1)]
    while queue:
        q, qs, qp = queue.popleft()
        if q == k:
            return qs, qp
        for move in (q - 1, q + 1, q * 2):
            if 0 <= move <= 100000 and not visited[move]:
                visited[move] = True
                np = qp + [move]
                queue.append([move, qs + 1, np])
                
second, paths = bfs(n)
print(second)
for p in paths:
    print(p, end=' ')
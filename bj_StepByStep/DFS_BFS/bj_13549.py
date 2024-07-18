# BFS로 탐색할 때 최단시간 등을 계산해야 한다면, 유리한 순서로 계산해야 최단시간 or 최단 거리를 찾을 수 있다.
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
MAX = 1000001
visited = [0 for _ in range(MAX)]

def bfs(n, k):
    queue = deque([])
    queue.append([n, 0])
    visited[n] = 1
    while queue:
        qn, cnt = queue.popleft()
        if qn == k:
            return cnt
        for i, index in enumerate([2 * qn, qn - 1, qn + 1]):
            if 0 <= index < MAX and visited[index] == 0:
                if i == 0:
                    queue.append([index, cnt])
                else:
                    queue.append([index, cnt + 1])
                visited[index] = 1
print(bfs(n, k))
# 예외처리를 못했음 
from collections import deque
n, k = map(int, input().split())
maxnum = 100000
visited = [False] * (maxnum+1)
def bfs(start, count):
    queue = deque([(start, count)])
    while queue:
        node, depth = queue.popleft()
        if node == k:
            return depth
        next1 = node + 1
        next2 = node - 1
        next3 = node * 2
        if 0 <= next1 <= maxnum and not visited[next1]:
            visited[next1] = True
            queue.append((next1, depth + 1))
        if 0 <= next2 <= maxnum and not visited[next2]:
            visited[next2] = True
            queue.append((next2, depth + 1))
        if 0 <= next3 <= maxnum and not visited[next3]:
            visited[next3] = True
            queue.append((next3, depth + 1))
            
time = bfs(n, 0)
print(time)
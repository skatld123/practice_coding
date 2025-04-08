# 순간이동

from collections import deque
# 1초 X-1, X +1 / 0초 2*X

# n 수빈, k 동생
n, k = map(int, input().strip().split())

visited = [-1 for _ in range(100001)]

def bfs(idx):
    queue = deque([])
    queue.append(idx)
    visited[idx] = 0
    while queue:
        qidx = queue.popleft()
        if qidx == k:
            return visited[qidx]
        
        double, left, right = qidx * 2, qidx - 1, qidx + 1
        
        if 0 <= double < len(visited) and visited[double] == -1:
            queue.append(double)
            visited[double] = visited[qidx]
            
        if 0 <= left < len(visited) and visited[left] == -1:
            queue.append(left)
            visited[left] = visited[qidx] + 1
            
        if 0 <= right < len(visited) and visited[right] == -1:
            queue.append(right)
            visited[right] = visited[qidx] + 1

print(bfs(n))

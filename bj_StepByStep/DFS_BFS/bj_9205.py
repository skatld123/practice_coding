import sys
from collections import deque

def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        qx, qy = queue.popleft()
        # 이동거리
        mx, my = abs(qx - dest[0]), abs(qy - dest[1])
        # 현재 위치에서 도착지까지 거리가 1000 이내라면, (맥주 20개 * 50m)
        if mx + my <= 1000:
            return "happy"
        for i in range(n): # 편의점 개수
            if not visited[i]:
                nx, ny = convs[i] # 편의점 좌표
                if abs(qx - nx) + abs(qy - ny) <= 1000:
                    visited[i] = True
                    queue.append([nx, ny])
    return "sad"

input = sys.stdin.readline
testCases = int(input().strip())
# 집, 편의점, 펜타포트 락 페스티벌
for t in range(testCases):
    convs = []
    n = int(input().strip())
    starts = list(map(int, input().strip().split()))
    for i in range(n):
        convs.append(list(map(int, input().strip().split())))
    dest = list(map(int, input().strip().split()))
    # 편의점 방문 여부
    visited = [False for _ in range(n+1)]
    print(bfs(starts[0], starts[1]))


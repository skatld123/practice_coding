import sys
sys.setrecursionlimit(10**6)
# m x n, k=rectangle
m, n, k = map(int, input().split())

graph = []
for i in range(m) :
    graph.append([0 for j in range(n)])
        
rects = []
# (y, x) (y(m)가 행, x(n)가 열) 
# 직사각형부터 먼저 그리기
for i in range(k) :
    y1, x1, y2, x2 = map(int, input().split())
    for y in range(y1, y2) :
        for x in range(x1, x2) :
            graph[x][y] = 1

count = 0
# 깊이 우선 탐색
def dfs(x, y) : 
    global count
    if x < 0 or x >= m or y < 0 or y >= n :
        return 0
    if graph[x][y] == 0 :
        graph[x][y] = 1
        count += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return count
    return 0

result = 0
areas = []
for i in range(m) :
    for j in range(n):
        area = dfs(i, j)
        if area :
            areas.append(area)
            count = 0
            
print(len(areas))
areas = sorted(areas)
for i in areas : 
    print(i, end=' ')
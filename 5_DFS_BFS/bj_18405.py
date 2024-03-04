# N -> 맵 크기, K -> 바이러스 종류 
# BFS
n, k = map(int, input().split())

test_map = []
for i in range(n):
    test_map.append(list(map(int, input().split())))

count = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] 
# DFS 사용
def dfs(x, y):
    print(test_map)
    global count 
    if x < 0 and x >= n and y < 0 and y >= n:
        return False
    if test_map[x][y] != 0:
        for x1, y1 in zip(dx, dy):
            if test_map[x][y] < test_map[x1][y1] or test_map[x1][y1] == 0:
                test_map[x1][y1] = test_map[x][y]
                dfs(x1, y1)
                return True
        count += 1
    return False
    
for i in range(n):
    for j in range(n):
        if test_map[i][j]:
            dfs(i, j, test_map[i][j])

print(test_map)
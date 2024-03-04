# 장애물을 세우고 세운 모든 경우에 수에 대해 bfs를 수행 (모든 위치 탐색)
# 탐색이 끝나면 O를 X로 초기한 후
n = int(input())
graph = []
teacher = []
isSuccess = False
for i in range(n):
    line = list(input().split())
    graph.append(line)
    for idx, pos in enumerate(line) :
        if pos == 'T' : teacher.append([i, idx])

def make_obstacle(cnt):
    global isSuccess
    if cnt == 3 :
        if bfs() :
            isSuccess = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    make_obstacle(cnt + 1)
                    graph[i][j] = 'X'

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for t in teacher:
        for nx, ny in zip(dx, dy):
            tx, ty = t
            while 0 <= tx < n and 0 <= ty < n :
                if graph[tx][ty] == 'O':
                    break
                if graph[tx][ty] == 'S':
                    return False
                tx += nx
                ty += ny
    return True

make_obstacle(0)
if isSuccess:
    print("YES")
else: print("NO")
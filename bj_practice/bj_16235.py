# r은 행 c는 열 1부터 시작
# 양분은 모든 칸에 5만큼있음
# 하나의 칸에 여러 나무가 있다면 어린 나무부터 먹음
# 봄 : 각 칸에 존재하는 양분만 먹고, 자신의 나이만큼 양분을 못먹으면 나무가 죽음
# 여름 : 봄에 죽은 나무가 양분으로 변함 (죽은 나무의 나이를 2로 나눈 값이 양분으로 추가됨)
# 가을 : 나무가 번식, 나이가 5의 배수여야 번식하며
# 인접한 8개의 칸에 나이가 1인 나무가 생성됨
# 겨울 :로봇이 돌아다니며 땅에 양분을 추가, A[r][c] 만큼 추가됨

# K 년 이후 살아있는 나무개수는??

# N, M, K


import sys

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
cnt = 0
robot = []
graph = [[5] * n for _ in range(n)]
tree_grp = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    robot.append(list(map(int, input().strip().split())))

for _ in range(m):
    x, y, age = map(int, input().strip().split())
    tree_grp[x - 1][y - 1].append(age)
    cnt += 1

dx, dy  = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

while k > 0:    
    dead_tree = []
    fall_tree = [] 

    # 한바퀴 돌면서 나무가 심어진 곳을 확인하고, 나이만큼 양분먹고 +1 하기
    for i in range(n):
        for j in range(n):
            if tree_grp[i][j]:
                trees = tree_grp[i][j]
                trees.sort()
                live_trees = []
                dead_tree = 0
                for tidx in range(len(trees)):
                    tage = trees[tidx]
                    if graph[i][j] - tage >= 0:
                        graph[i][j] = graph[i][j] - tage
                        tree_grp[i][j][tidx] += 1 # 나이증가
                        live_trees.append(tree_grp[i][j][tidx]) # 살아있는 놈들만 임시저장
                        if tree_grp[i][j][tidx] % 5 == 0:
                            fall_tree.append([i, j])
                    else: # 죽은 나무 
                        dead_tree += tage // 2
                        cnt -= 1
                tree_grp[i][j] = live_trees
                graph[i][j] += dead_tree

    # fall
    for ft in fall_tree:
        x, y = ft
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                tree_grp[nx][ny].append(1)
                cnt += 1

    # winter
    for i in range(n):
        for j in range(n):
            graph[i][j] += robot[i][j]
    k -= 1
print(cnt)

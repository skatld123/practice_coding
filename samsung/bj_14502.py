# 시간초과 문제임 
import sys
from collections import deque
import copy

input = sys.stdin.readline

# 벽을 세워서 막자
# 세로 n, 가로 m
n, m = map(int, input().rstrip().split())

# 0 빈칸 ,1벽 , 2바이러스
lab = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 안전영역의 최대를 구할 것 , 벽을 새롭게 3개를 꼭 세워야 함
# 바이러스는 얖옆으로 퍼져나감

# 벽을 세워야하는 함수(backtrack), 바이러스 퍼지는 함수
# 벽을 하나씩 다 세워 보면서, 그때 마다 영역을 퍼뜨려보고, 안전영역 넓이를 구하면 될듯
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def backtrack(build_cnt):
    if build_cnt == 3:
        split_virus()
        return
    for i in range(n):
        for j in range(m):
            if 0 <= i < n and 0 <= j < m and lab[i][j] == 0:
                lab[i][j] = 1
                backtrack(build_cnt + 1)
                lab[i][j] = 0

# 바이러스 퍼지기
def split_virus():
    queue = deque([])
    temp_lab = copy.deepcopy(lab)
    # 바이러스 시작지점
    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 2:
                queue.append([i, j])
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append([nx, ny])

    global maximum
    cnt = 0
    for i in range(n):
        cnt += temp_lab[i].count(0)
    maximum = max(maximum, cnt)
    return

maximum = 0
backtrack(0)
print(maximum)

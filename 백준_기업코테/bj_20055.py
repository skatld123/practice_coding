# 1번 올리는 위치 n번 내리는 위치
# 로봇이 올리거나 어떤 칸으로 이동하면 내구도 감소


# 벨트가 각 칸위에 있는 로봇과 함칸 회전
# 칸의 내구도가 남아 1 이상 남아있고 앞칸에 로봇이 없으면 가능
# 1번에 로봇을 올림 (1번이 0 이 아니면)
# 0개의 내구도가 K개 이상이면 과정 종료
from collections import deque

# 길이 n, 끝나는 기준 k
n, k = map(int, input().strip().split())

# 일단 벨트를 2n으로 만듬
# n-1까지가 위에 줄, 2n -1가 올리기 전
belt = deque(list(map(int, input().strip().split())))

robot_list = deque([False for _ in range(n)])
# 한 동작씩 이동하는 반복문을 만들 것
count = 0
start_idx = 0
end_idx = n - 1

stage = 1
# robot_index = []
while True:
    belt.rotate(1)
    robot_list.rotate(1)
    robot_list[-1] = False  # 로봇 내리기

    for i in range(len(robot_list) - 1, 0, -1):
        if robot_list[i - 1] and not robot_list[i] and belt[i] >= 1:
            robot_list[i - 1] = False
            robot_list[i] = True
            belt[i] -= 1

            if belt[i] == 0:
                count += 1

    robot_list[-1] = False  # 로봇 내리기

    # 로봇 올리기
    if belt[0] > 0:
        robot_list[0] = True
        belt[0] -= 1

        if belt[0] == 0:
            count += 1

    # 4stage
    if count >= k:
        break
    else:
        stage += 1

print(stage)

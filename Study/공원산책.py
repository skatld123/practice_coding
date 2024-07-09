from collections import deque


def solution(park, routes):
    answer = []
    sx, sy = 0, 0
    for i in range(len(park)):
        if "S" in park[i]:
            sx = i
            sy = park[i].index("S")

    queue = deque(routes)
    while queue:
        direction, move = queue.popleft().split()
        isWall, isOut = False, False
        nx, ny = sx, sy
        for i in range(int(move)):
            if direction == "N":
                nx -= 1
            elif direction == "S":
                nx += 1
            elif direction == "W":
                ny -= 1
            elif direction == "E":
                ny += 1
            if not (0 <= nx < len(park) and 0 <= ny < len(park[0])):
                isOut = True
                break
            if park[nx][ny] == "X":
                isWall = True
                break
        if not isOut and not isWall:
            sx, sy = nx, ny
    return [sx, sy]

from collections import deque

def solution(n, info):
    answer = []
    lion = bfs(n, info)
    if not lion:
        answer.append(-1)
    else:
        answer = lion[0]
    return answer

def bfs(n, info):
    result = []
    queue = deque([[0, [0] * len(info)]])
    maximum = 0
    while queue:
        qn, qinfo = queue.popleft()
        # 화살의 수가 많으면 그만두기
        if sum(qinfo) < n and qn != 10:
            # 화살을 더 많이 맞추기
            qinfo1 = qinfo[:]
            qinfo1[qn] = info[qn] + 1
            queue.append([qn + 1, qinfo1])

            # 화살 안맞추기 (0개)
            qinfo2 = qinfo[:]
            qinfo2[qn] = 0
            queue.append([qn + 1, qinfo2])
        # 점수계산
        elif sum(qinfo) == n:
            peach, lion = 0, 0 # qinfo 라이언, info 어피치
            for i in range(11):
                if not (info[i] == 0 and qinfo[i] == 0):
                    if qinfo[i] <= info[i]:
                        peach += (10 - i) 
                    else:
                        lion += (10 - i) 
            if lion > peach:
                if maximum < (lion - peach):
                    maximum = (lion - peach)
                    result.clear()
                    result.append(qinfo)
        elif qn == 10:
            qinfo1 = qinfo[:]
            qinfo1[qn] = n - sum(qinfo1)
            queue.append([-1, qinfo1])
    return result

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
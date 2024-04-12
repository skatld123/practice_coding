from collections import deque
from copy import deepcopy

def solution(tickets):
    answer = []
    # 인천 공항 스타트
    
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            paths = bfs(i, tickets)
            for p in paths:
                answer.append(p) # 모두 티켓썼는지 확인이 필요
    
    answer.sort()
    return answer[0]

def checkTrue(used):
    flag = True
    for i in used:
        if not i: return False
    return flag

def bfs(start_node, tickets):
    queue = deque() # ["ICN", "--"]
    used = [False] * len(tickets)
    used[start_node] = True
    all_paths = []
    queue.append([tickets[start_node], ["ICN"], used])
    while queue:
        (depart, arrival), paths, q_used = queue.popleft()
        if len(paths) == len(tickets) and checkTrue(q_used):
            paths.append(arrival)
            all_paths.append(paths)
        for i in range(len(tickets)):
            if arrival == tickets[i][0] and not q_used[i]:
                print(paths)
                tmp_used = q_used[:]
                tmp_used[i] = True
                print(tmp_used) 
                queue.append([tickets[i], paths + [arrival], tmp_used])
    return all_paths

print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
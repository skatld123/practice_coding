from collections import deque


def solution(priorities: list, location):
    answer = 0
    idx_list = [i for i in range(len(priorities))]
    queue = deque(priorities)
    idx_list = deque(idx_list)
    target = idx_list[location]

    while target in idx_list:
        q = queue.popleft()
        idx = idx_list.popleft()
        isBigger = False
        for nq in queue:
            if q < nq:
                print(q, nq)
                isBigger = True
                break

        if isBigger:
            queue.append(q)
            idx_list.append(idx)
        else:
            answer += 1
    return answer

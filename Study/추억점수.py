from collections import deque
def solution(name, yearning, photo):
    answer = []
    ny_dict = {}
    for i in range(len(name)):
        ny_dict[name[i]] = yearning[i]
    
    for p in photo:
        queue = deque(p)
        score = 0
        while queue:
            qname = queue.popleft()
            if qname in ny_dict.keys():
                score += ny_dict[qname]
        answer.append(score)                
    return answer
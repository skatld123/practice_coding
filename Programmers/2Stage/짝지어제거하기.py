def solution(s):
    answer = -1
    slist = list(s)
    stack = []
    for i in range(len(slist)):
        if len(stack) == 0:
            stack.append(slist[i])
        elif slist[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(slist[i])
            
    if len(stack) == 0:
        answer = 1
    else: answer = 0
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3
import sys
sys.setrecursionlimit(10**8)
def solution(p):
    answer = ''
    
    if not p:
        return answer
    # 균형잡힌 괄호 문자열로 분리하는 방법
    p_list = list(p)
    answer = dfs(p_list)
    answer = ''.join(map(str, answer))
    print(answer)
    return answer

    
def dfs(p):
    l_cnt = 0
    r_cnt = 0
    stack = []
    balance = False
    if not p:
        return ''
    else: p = list(p)
    for idx, cha in enumerate(p):
        if cha == "(":
            l_cnt += 1
            stack.append(cha)
        else: 
            r_cnt += 1
            if len(stack) != 0:
                stack.pop()
        if r_cnt == l_cnt: 
            if len(stack) == 0: balance = True
            break
    u, v = p[:(r_cnt + l_cnt)], p[(r_cnt + l_cnt):]
    if balance:
        x = dfs(v)
        if isinstance(x, list):
            for _x in x :
                u.append(_x)
        else : u.append(x)
        return u 
    else:
        a = ['(']
        x = dfs(v)
        if isinstance(x, list):
            for _x in x :
                a.append(_x)
        else : a.append(x)
        a.append(')')
        u.pop()
        u.pop(0)
        for _u in u:
            if _u == '(':
                a.append(')')
            else: a.append('(')
        return a

solution("()))((()")
solution(")(")
solution("()))((()")
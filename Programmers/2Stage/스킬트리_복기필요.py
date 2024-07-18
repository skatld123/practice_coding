def solution(skill, skill_trees):
    answer = 0
    for skt in skill_trees:
        s = ""
        for ch in skt:
            if ch in skill:
                s += ch
        if skill[:len(s)] == s:
            answer += 1
    return answer
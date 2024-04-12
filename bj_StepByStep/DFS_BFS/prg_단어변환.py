from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words) # 방문한 문자열인지 확인
    
    queue = deque([[begin, 0]])
    while queue:
        qword, stage = queue.popleft()
        if qword == target:
            return stage
        
        for idx in range(len(words)):
            if check(qword, words[idx]) and not visited[idx]:
                visited[idx] = True
                queue.append([words[idx], stage+1])

    return answer

#   우선 words에 있는 단어가 begin과 다른 글자가 몇개가 되는지에 대한 메서드
def check(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    cnt = 0
    for idx in len(word1):
        if word1[idx] != word2[idx]:
            cnt += 1
    if cnt == 1: return True
    else: return False
    
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
def solution(s):
    answer = -1
    # 0부터 s길이 만큼 for문을 반복
    # 문자열을 조합해보고 해당 문자열을 Stack에 넣기
    open = ["[", "{", "("]
    closed = ["]", "}", ")"]
    wrong = 0
    for i in range(len(s)):
        stack = []
        st = s[i:] + s[:i]
        for j in range(len(st)):
            if st[j] in open:
                stack.append(st[j])
            elif st[j] in closed:
                if not stack:
                    wrong += 1
                    break
                else:
                    opened = stack.pop()
                    if open.index(opened) != closed.index(st[j]):
                        wrong += 1
                        break
            if j == (len(st) - 1) and len(stack) != 0: wrong += 1
    answer = len(s) - wrong
    return answer


from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([[0, 0]])
    length = len(numbers)
    while queue:
        q, idx = queue.popleft()
        if (idx + 1) < length:
            minus = q - numbers[idx + 1]
            plus = q + numbers[idx + 1]
            queue.append([minus, idx + 1])
            queue.append([plus, idx + 1])
        else:
            if target == q:
                answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))
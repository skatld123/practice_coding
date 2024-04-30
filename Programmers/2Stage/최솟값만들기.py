# DP로 풀려다가 문제를 깨달음 -> 문제를 먼저 이해하려고 노력할 것
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += (A[i] * B[i])
    return answer
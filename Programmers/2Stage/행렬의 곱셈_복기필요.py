# 플로이드 워셜 기억하기..
def solution(arr1, arr2):
    answer = [[]]
    arr1_i = len(arr1)
    arr1_j = len(arr1[0])
    arr2_j = len(arr2)
    arr2_k = len(arr2[0])
    answer = [[0] * arr2_k for _ in range(arr1_i)]
    # (i,j)   (j,k)  ->  (i,k)
    for i in range(arr1_i):
        for k in range(arr2_k):
            for j in range(arr2_j):
                answer[i][k] += arr1[i][j] * arr2[j][k]
            
    return answer
def solution(brown, yellow):
    answer = []
    all_color = brown + yellow
    # x를 반복문 돌고, y 반복문 돌며 각 조건에 충족하는지 확인
    # yw * yh = yellow, 
    # bw = yw + 2, bh = yh + 2
    # brown = bw * bh - yellow, 2bw + 2bh - 4
    # i가 가로, j가 세로
    for i in range(1, all_color + 1):
        j = all_color // i
        if i >= j:
            if i * j == all_color and (2*i + 2*j - 4) == brown:
                return [i, j]
        elif j > i:
            continue
        else:
            continue
    return answer
def solution(n):
    answer = 0
    bn = format(n, 'b')
    bnlist = list(map(int, bn))
    one_cnt = bnlist.count(1)
    while True:
        n += 1
        nbn = format(n, 'b')
        nbnlist = list(map(int, nbn))
        none_cnt = nbnlist.count(1)
        if one_cnt == none_cnt:
            answer = ''.join(map(str, nbnlist))
            answer = int(answer, 2)
            break
    return answer
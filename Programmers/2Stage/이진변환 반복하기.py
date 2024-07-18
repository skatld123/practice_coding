def solution(s):
    answer = []
    cnt = 0
    remove_zero_cnt = 0
    slist = list(s)
    while True:
        if slist == ['1']:
            break
        slist, zcnt = transform(slist)
        cnt += 1
        remove_zero_cnt += zcnt
    answer = [cnt, remove_zero_cnt]
    return answer

def transform(slist):
    one_cnt = ""
    for s in slist:
        if s == "1":
            one_cnt += s
    c = len(one_cnt)
    binary = format(c, 'b')
    return list(binary), len(slist) - c
    
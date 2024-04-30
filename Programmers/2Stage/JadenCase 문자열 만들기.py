def solution(s):
    answer = ''
    slist = s.split(' ')
    for i in range(len(slist)):
        wlist = list(slist[i])
        if len(wlist) > 0:
            if not wlist[0].isdigit():
                wlist[0] = wlist[0].upper()
            for j in range(1, len(wlist)):
                wlist[j] = wlist[j].lower()
            slist[i] = ''.join(wlist)
    answer = ' '.join(slist)
    return answer
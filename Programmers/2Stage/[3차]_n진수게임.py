def makeNum(num, n):
    nlist = []
    chars = "0123456789ABCDEF"
    if num == 0:
        return ['0']
    while num > 0:
        remain = num % n
        nlist.append(chars[remain])
        num = num // n
    nlist.reverse()
    return nlist

def solution(n, t, m, p):
    answer = ''
    # n진법, t의 개수, m 인원, p 순서
    # m인원 * t 만큼 반복할 것 10진수로 배열짜기
    nlist = []
    for i in range(t * m):
        nlist += makeNum(i, n)
    index = p
    for i in range(t):
        answer += str(nlist[index - 1])
        index += m
    return answer


            
        
def solution(s):
    answer = []
    # 크기 1인 것부터 -> 2 -> 3 순서로 맞춰가면 됨 
    # 크기 1일때는 그게 맨 앞, 2에서는 나머지 원소가 뒤, 
    # 일단 문자열을 리스트로 변환
    s = s[2:-2]
    slist = s.split("},{")
    nlist = []
    for i in range(len(slist)):
        nlist.append(list(map(int, slist[i].split(","))))
    nlist.sort(key=lambda x : len(x))
    for i in range(len(nlist)):
        if i == 0: 
            answer.append(nlist[i][0])
        else:
            for jn in nlist[i]:
                if not jn in answer:
                    answer.append(jn)
    return answer
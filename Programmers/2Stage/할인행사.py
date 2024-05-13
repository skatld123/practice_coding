def solution(want, number, discount):
    # 만약 want가 discount에 없다면 0을 return
    # discount의 하루씩 for문 하기 + 10일까지의 과일 개수 세서 빼기
    wrong = 0
    for i in range(len(discount)):
        want_dic = dict(zip(want, number))
        if i + 10 > len(discount):
            new_discount = discount[i:]
        else:
            new_discount = discount[i:i+10]
        for dis in new_discount:
            if dis in want_dic.keys():
                want_dic[dis] -= 1
        for v in want_dic.values():
            if v > 0: 
                wrong += 1
                break
    return len(discount) - wrong
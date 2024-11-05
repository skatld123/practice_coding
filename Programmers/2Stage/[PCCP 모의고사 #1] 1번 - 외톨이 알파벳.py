def solution(input_string):
    dicts = {}
    answer = ""
    for idx, cha in enumerate(input_string):
        if cha in answer:
            dicts[cha].append(idx)
            continue
        if not cha in dicts:
            dicts[cha] = [idx]
        else:
            # 이미 있다는 것은 안에 2번 이상 나온 것
            # 즉, 내부 요소와 현재 idx와의 거리가 얼마나 차이나는지 확인이 필요
            # 외톨이 문자열이라면 (가장 최근 인덱스와의 거리를 비교)
            if idx - dicts[cha][-1] > 1:
                answer += cha
            dicts[cha].append(idx)
    if not answer:
        return "N"
    return "".join(sorted(answer))

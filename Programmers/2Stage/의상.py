# 경우의 수 못구해서 틀렸음
def solution(clothes):
    answer = 1
    clothes_dic = {}
    for cloth, type in clothes:
        if type in clothes_dic.keys():
            clothes_dic[type].append(cloth)
        else:
            clothes_dic[type] = [cloth]
    # 모든 경우의 수대로 다 입지 않음
    # 2개씩 입을때도 있고, 3개씩도 있음
    for type, clist in clothes_dic.items():
        answer = answer * (len(clist) + 1)
    return answer - 1
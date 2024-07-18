import collections
# 1. collections.Counter를 이용하여 리스트 중복 요소 개수 확인
# 2. sorted를 이용하여 dic을 원하는대로 정렬함
def solution(k, tangerine):
    answer = 0
    # 귤을 오름차순으로 정렬
    # k보다 가장 많은 수의 귤이 작다면 넣기, 
    # 남은 공간만큼 많은 수 더 넣어보기
    # 만약 k가 꽉찬다면 종류의 개수를 세어보기
    tan_dic = collections.Counter(tangerine)
    tan_dic = sorted(tan_dic.items(), key=lambda x : (-x[1], x[0]))
    for att in tan_dic:
        if k == 0: break
        if att[1] <= k:
            k -= att[1]
            answer += 1
        else: # 만약 k개 이상이면 한가지로 통일 가능하다는 뜻
            answer += 1
            return answer
    return answer
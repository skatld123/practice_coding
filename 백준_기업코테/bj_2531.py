# 초밥 종류가 번호
# k 개 연속해서 먹으면 할인
# 1번행사에 참여하면 쿠폰에 적힌 초밥 무료 제공
# 벨트위에 없으면 요리사가 새로 만듬

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 
# 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().strip().split())
sushi = []
for _ in range(N):
    sushi.append(int(input().strip()))

sushi = sushi * 2

maximum = 0
for i in range(N):
    food_list = sushi[i : i + k]
    food_list.append(c)
    cnt = len(list(set(food_list)))
    maximum = max(maximum, cnt)

print(maximum)

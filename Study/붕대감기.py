from collections import deque


def solution(bandage, health, attacks):
    answer = 0
    # 체력이 0 이하가 되면 캐릭터가 죽음
    # t초동안 1초에 x만큼 회복, t초 연속으로 한다면 +y 회복
    # 취소하자마자 다시 붕대감기를 시전
    # 연속 성공시간이 0으로 초기화됨
    # 죽으면 -1 , 마지막 체력을 Return
    # bandage t, x, y
    # attack 공격시간, 피해량
    attacks = deque(attacks)
    init_health = health
    ht, hx, hy = bandage
    time = 0
    healCnt = 0
    while attacks:
        time += 1
        if attacks[0][0] == time:
            at_time, at_dmg = attacks.popleft()
            health -= at_dmg
            if health <= 0:
                return -1
            healCnt = 0
        else:
            healCnt += 1
            if health < init_health:
                health += hx
                if healCnt == ht:
                    health += hy
            if health > init_health:
                health = init_health
    return health

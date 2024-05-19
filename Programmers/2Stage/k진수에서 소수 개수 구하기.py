# 루트를 생각할 것
def solution(n, k):
    answer = 0
    k_num = ""
    while n:
        k_num += str(n % k)
        n = n // k 
    k_num = k_num[::-1]
    k_list = k_num.split("0")
    for i in range(len(k_list)):
        if len(k_list[i]) == 1 and not k_list[i] == '1':
            answer += 1
        elif k_list[i].isdigit() and not k_list[i] == '1':
            kn = int(k_list[i])
            isTrue = False
            for j in range(2, int(kn**(1/2)+1)):
                if kn % j == 0:
                    isTrue = True
                    break
            if not isTrue:
                answer += 1
    return answer
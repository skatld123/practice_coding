'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# import sys
# sys.stdin = open("sample_input.txt", "r")

"aba /c/ aba"
"abcd /e/ dcba"
def isPalindrome(string):
    length = len(string)
    # 홀수일 때, 앞의S와 뒤에 S가 같은지 확인
    if length % 2 != 0:
        front = string[:((length - 1) // 2)]
        back = string[((length - 1) // 2) + 1:]
        if front == back:
            return front, back, True
    else: # 짝술때
        front = string[:(length // 2)]
        back = string[(length // 2):]
        if front == back:
            return front, back, True
    return front, back, False

# # abba -> 3/2 = 1,
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
test_case = "abacaba"
test_case = "abaaba"
front, back, isPalin = isPalindrome(test_case)  # "aba /c/ aba"
if isPalin:
    _, _, isFront = isPalindrome(front)
    _, _, isBack = isPalindrome(back)
    if isFront and isBack:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
else:
    print(f"#{test_case} NO")

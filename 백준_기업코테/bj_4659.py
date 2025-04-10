# 모음 5개 중 하나 반드시 포함
# 모음 3개 , 자음 3개 연속 금지
# 같은 글자 연속 2개 안되지만 ee , oo 허용

moem = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input().strip()
    if pw == 'end':
        break

    isPass = False
    for m in moem:
        if m in pw:
            isPass = True
            break

    isTriple = True
    if len(pw) > 2:
        for i in range(2, len(pw)):
            one, two, three = pw[i] in moem, pw[i - 1] in moem, pw[i - 2] in moem
            if one == two == three:
                isTriple = False
                break
            else:
                isTriple = True
    else:
        isTriple = True

    isChain = True
    if len(pw) > 1:
        for i in range(1, len(pw)):
            if pw[i - 1] == pw[i]:
                if pw[i] == 'o' or pw[i] == 'e':
                    isChain = True
                else:
                    isChain = False
                    break

    else:
        isChain = True

    if isPass and isChain and isTriple:
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")

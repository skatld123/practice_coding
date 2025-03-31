msg = "ABCDEF"
# ABCDEF
# 012345
# DEBFCA
# 341520

# 0-1,2
# 1-3,4
# 2-5

answer = ""


# 후위 순회 함수
def postorder_traversal(index, nodes):
    global answer
    if index >= len(nodes):  # 범위를 벗어나면 종료
        return
    # 왼쪽 자식에 대해 재귀 호출
    postorder_traversal(2 * index + 1, nodes)
    # 오른쪽 자식에 대해 재귀 호출
    postorder_traversal(2 * index + 2, nodes)
    # 현재 노드 값을 answer에 추가
    answer += nodes[index]


# 암호화 함수
def encrypt_message(message):
    global answer
    answer = ""  # 초기화
    nodes = list(message)  # 메시지를 리스트로 변환
    postorder_traversal(0, nodes)  # 루트 노드부터 후위 순회 시작
    return answer


# 테스트
message = "ABCDEF"
print(encrypt_message(message))  # 출력: "DEBFCA"

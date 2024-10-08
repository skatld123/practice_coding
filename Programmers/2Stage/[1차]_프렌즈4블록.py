def solution(m, n, board):
    answer = 0
    new_board = []
    # 보드 문자열을 리스트로 변환
    for i in range(m):
        new_board.append(list(board[i]))
    cnt = 0
    while True:
        # 각 블록을 순회하면서 2x2를 검색
        block_list = set([])
        for i in range(m):
            for j in range(n):
                if new_board[i][j] != "*":
                    blocks = check_2x2(i, j, new_board, m, n)
                    if blocks:
                        block_list.update(blocks)

        if len(block_list) == 0:
            break

        block_list = sorted(block_list, key=lambda x: (x[1], x[0]))
        # 블록을 이용해서 땡겨오기,,
        for bx, by in block_list:
            for k in range(bx, 0, -1):
                new_board[k][by] = new_board[k - 1][by]
            new_board[0][by] = "*"

        answer += len(block_list)
    return answer


def check_2x2(qx, qy, board, m, n):
    char = board[qx][qy]
    dx, dy = [0, 1, 1], [1, 0, 1]
    blocks = [(qx, qy)]
    for i in range(len(dx)):
        nx, ny = qx + dx[i], qy + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == char:
            blocks.append((nx, ny))
        else:
            break
    if len(blocks) == 4:
        return blocks
    else:
        return None

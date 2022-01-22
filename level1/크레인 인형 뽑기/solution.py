def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        for select_board in board:
            extraction = select_board[i-1]
            if extraction == 0:
                pass
            else:
                if box and extraction == box[-1]:
                    answer += 2
                    box.pop()
                else:
                    box.append(extraction)
                select_board[i-1] = 0
                break
    return answer

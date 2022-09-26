def solution(board, moves):
    answer = 0
    pick_list = []

    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                pick_list.append(row[move - 1])
                row[move - 1] = 0

                if len(pick_list) > 1:
                    if pick_list[-1] == pick_list[-2]:
                        pick_list.pop(-1)
                        pick_list.pop(-1)

                        answer += 2
                break

    return answer
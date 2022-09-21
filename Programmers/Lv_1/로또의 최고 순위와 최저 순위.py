def solution(lottos, win_nums):

    cnt = 0

    for num in lottos:
        if num in win_nums:
            cnt = cnt + 1

    zero = lottos.count(0)

    rank = [6, 6, 5, 4, 3, 2, 1]

    answer = [rank[zero + cnt], rank[cnt]]

    return answer


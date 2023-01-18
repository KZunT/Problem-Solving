from itertools import permutations


def solution(k, dungeons):
    case_list = list(permutations(dungeons))

    res = []

    for case in case_list:
        cnt = 0
        piro = k
        for d in case:
            if d[0] <= piro:
                piro -= d[1]
                cnt += 1
        res.append(cnt)

    return max(res)
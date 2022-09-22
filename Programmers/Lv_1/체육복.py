def solution(n, lost, reserve):

    dup = set(reserve) & set(lost)
    reserve = list(set(reserve) - set(dup))
    lost = list(set(lost) - set(dup))

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
            continue
        elif i + 1 in lost:
            lost.remove(i + 1)

    answer = n - len(lost)

    return answer
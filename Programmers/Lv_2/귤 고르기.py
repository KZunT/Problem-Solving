from collections import Counter


def solution(k, tangerine):
    answer = 0
    kind = 0
    sell_tangerine = Counter(tangerine)

    for t, num in sorted(sell_tangerine.items(), key=lambda x: -x[1]):
        answer += 1
        kind += num
        if kind >= k:
            break

    return answer
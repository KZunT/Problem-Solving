def solution(k, score):
    answer = []
    fame = []
    for s in score:
        if len(fame) >= k:
            if min(fame) < s:
                fame[fame.index(min(fame))] = s
        else:
            fame.append(s)

        answer.append(min(fame))

    return answer

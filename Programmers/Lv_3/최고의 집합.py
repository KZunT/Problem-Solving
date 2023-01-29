def solution(n, s):
    q, r = divmod(s, n)

    if q == 0:
        return [-1]

    answer = [q] * n

    for i in range(r):
        answer[i] += 1

    answer.sort()

    return answer
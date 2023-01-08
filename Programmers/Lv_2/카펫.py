def solution(brown, yellow):
    answer = []

    # i 가로 j 세로

    for i in range(brown):
        for j in range(brown):
            if i * j == brown + yellow and ((i - 2) * (j - 2)) == yellow:
                answer = [max(i, j), min(i, j)]
    return answer

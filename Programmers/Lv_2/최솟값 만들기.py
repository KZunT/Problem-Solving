def solution(A, B):
    answer = 0

    for i, j in zip(sorted(A), reversed(sorted(B))):
        answer += i * j

    return answer

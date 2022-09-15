def solution(n):
    tmp = ''

    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)  # int 함수가 진법변환이 가능

    return answer
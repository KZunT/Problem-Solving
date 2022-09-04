def solution(x):
    answer = True

    x_sum = sum([int(i) for i in str(x)])

    if x % x_sum != 0:
        answer = False

    return answer
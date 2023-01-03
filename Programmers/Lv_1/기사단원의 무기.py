def divisor(num, limit, power):
    cnt = 0
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            cnt += 2
            if ((i ** 2) == num):
                cnt -= 1
        if cnt > limit:
            return power
    return cnt


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        answer += divisor(i, limit, power)
    return answer

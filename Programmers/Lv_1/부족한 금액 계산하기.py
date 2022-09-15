def solution(price, money, count):
    count_sum = sum(list(range(1, count + 1)))
    need = money - count_sum * price

    if need >= 0:
        return 0
    else:
        return -need
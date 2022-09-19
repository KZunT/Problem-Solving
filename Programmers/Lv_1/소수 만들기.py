import itertools


def is_prime(num):
    sq = int(num ** (1 / 2)) + 1
    for i in range(2, sq):
        if num % i == 0:
            return False
    return True


def solution(nums):

    result = []
    comb = list(map(sum, itertools.combinations(nums, 3)))

    for num in comb:
        if is_prime(num):
            result.append(num)

    answer = len(result)

    return answer
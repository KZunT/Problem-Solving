import itertools


def solution(numbers):

    num_list = list(itertools.combinations(numbers, r=2))
    sum_list = list(map(sum, num_list))
    sum_list = list(set(sum_list))
    sum_list.sort()

    return sum_list
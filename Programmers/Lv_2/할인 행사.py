from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_dict = dict()

    for w, n in zip(want, number):
        want_dict[w] = n

    for i in range(len(discount) - 9):
        if Counter(want_dict) == Counter(discount[i:i + 10]):
            answer += 1
    return answer
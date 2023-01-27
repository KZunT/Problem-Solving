from collections import Counter


def solution(topping):
    answer = 0
    left_topping = set()
    right_topping = Counter(topping)

    for t in topping:
        right_topping[t] -= 1
        left_topping.add(t)

        if right_topping[t] == 0:
            right_topping.pop(t)

        if len(left_topping) == len(right_topping):
            answer += 1

    return answer
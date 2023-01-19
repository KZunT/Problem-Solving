from itertools import product


def solution(word):
    answer = []
    word_list = ['A', 'E', 'I', 'O', 'U']

    # for i in range(1,6):
    #     pro =list(product(word_list,repeat = i))
    #     for p in pro:
    #         answer.append(''.join(p))

    answer = ["".join(p) for i in range(1, 6) for p in product(["A", "E", "I", "O", "U"], repeat=i)]
    answer.sort()

    return answer.index(word) + 1
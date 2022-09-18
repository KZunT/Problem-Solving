#에라토스테네스의 체


def solution(n):
    answer = []
    #     for i in range(2,n+1):
    #         prime = 1

    #         for j in range(2,i):

    #             if i % j == 0:

    #                 prime = 0

    #         if prime == 1:
    #             answer.append(i)

    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            answer.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

    return len(answer)
import sys

input = sys.stdin.readline


def solution(n, i, j):
    if n == 0:
        return

    cnt = (j - i + 1) // 3

    solution(n - 1, i, i + cnt - 1)

    for k in range(i + cnt, i + cnt * 2):
        answer[k] = ' '

    solution(n - 1, i + cnt * 2, i + cnt * 3 - 1)


while True:
    try:
        N = int(input())
        answer = ['-'] * (3 ** N)
        solution(N, 0, 3 ** N - 1)
        print(''.join(answer))
    except:
        break

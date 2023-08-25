import sys

T = int(input())

numbers = [True for _ in range(1000001)]

for i in range(2, 1001):
    if numbers[i]:
        for j in range(i + i, 1000001, i):
            numbers[j] = False

for _ in range(T):
    answer = 0
    N = int(sys.stdin.readline().rstrip())

    for i in range(2, N // 2 + 1):
        if numbers[i] and numbers[N - i]:
            answer += 1
    print(answer)

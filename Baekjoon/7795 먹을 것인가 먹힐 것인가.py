import bisect

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    answer = 0

    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    for num in A:
        answer += bisect.bisect(B, num - 1)

    print(answer)

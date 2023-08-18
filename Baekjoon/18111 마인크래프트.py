import sys

N, M, B = map(int, sys.stdin.readline().split())
block = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 10 ** 8
floor = 0

for idx in range(257):
    max_target, min_target = 0, 0

    for i in range(N):
        for j in range(M):
            if block[i][j] >= idx:
                max_target += block[i][j] - idx
            else:
                min_target += idx - block[i][j]

    if max_target + B >= min_target:
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2)
            floor = idx

print(answer, floor)

#pypy3
from itertools import combinations

N, M, K = map(int, input().split())

nums = [i for i in range(N)]
answer = 0
cases = [*combinations(nums, M)]

for case in cases:
    cnt = 0
    for idx in range(M):
        if case[idx] < M:
            cnt += 1
    if cnt >= K:
        answer += 1

print(answer / len(cases))

# 시간초과
# from itertools import product
#
# N, M = map(int, input().split())
#
# num_list = list(range(1, N + 1))
#
# res = product(num_list, repeat=M)
#
# for r in res:
#     if list(r) == sorted(list(r)):
#         print(' '.join(list(map(str, r))))

n, m = map(int, input().split())

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)  # 1부터 순서대로 호출
# 메모리 초과..

# import itertools
#
# N = int(input())
# seek_perm = tuple(map(int, input().split(' ')))
# N_list = list(range(1, 1+N))
#
# perm_list = list(itertools.permutations(N_list, N))
#
# p_idx = perm_list.index(seek_perm)
#
# if p_idx == 0:
#     print(-1)
# else:
#     print(*perm_list[p_idx-1])

N = int(input())
seek_perm = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if seek_perm[i] < seek_perm[i - 1]:
        x, y = i-1, i
        for j in range(N-1, 0, -1):
            if seek_perm[j] < seek_perm[x]:
                seek_perm[j], seek_perm[x] = seek_perm[x], seek_perm[j]
                seek_perm = seek_perm[:i] + sorted(seek_perm[i:], reverse=True)
                print(*seek_perm)
                exit(0)
print(-1)
from itertools import permutations

N, M = map(int, input().split())

arr = range(1,N+1)
permu = permutations(arr,M)

for p in permu:
    print(' '.join(map(str,p)))
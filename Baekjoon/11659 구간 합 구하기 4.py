# 구간합 prefix sum 을 이용

import sys
N,M = map(int, sys.stdin.readline().split())

pfs = list(map(int,sys.stdin.readline().split()))

for i in range(N - 1):
    pfs[i+1] += pfs[i]
pfs = [0] + pfs

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    print(pfs[b]-pfs[a-1])
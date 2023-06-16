N, K = map(int, input().split())

bucket = K * (K + 1) // 2

if N < bucket:
    print(-1)
elif (N - bucket) % K == 0:
    print(K - 1)
else:
    print(K)

N, K = map(int, input().split())
numbers = [False] * (N + 1)

cnt = 0

for i in range(2, N + 1):
    if numbers[i] == False:
        for j in range(i, N + 1, i):
            if numbers[j] == False:
                numbers[j] = True
                cnt += 1
                if cnt == K:
                    print(j)

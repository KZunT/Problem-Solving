N = int(input())

arr = list(map(int, input().split()))

res = []

for i in range(N - 2, -1, -1):
    if arr[i + 1] > arr[i]:
        idx = 0
        for j in range(i + 1, N):
            if arr[i] < arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
        res += arr[:i + 1]
        res += arr[i + 1:][::-1]

        print(" ".join(map(str, res)))
        break

else:
    print(-1)

N = int(input())
arr = list(map(int, input().split()))

dec = [1] * N
inc = [1] * N

for i in range(1, N):
    if arr[i] >= arr[i - 1]:
        inc[i] = max(inc[i], inc[i - 1] + 1)

    if arr[i] <= arr[i - 1]:
        dec[i] = max(dec[i], dec[i - 1] + 1)

print(max(max(inc), max(dec)))

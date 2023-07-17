N = int(input())
cnt = 0

for i in range(1, N):
    if i * 2 < N <= i * 3:
        cnt += i - (N - i - 1) // 2

print(cnt)

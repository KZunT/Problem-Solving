N, M = map(int, input().split())
result = []

for _ in range(N):
    a, b = map(int, input().split())
    miles = list(map(int, input().split()))
    miles.sort(reverse=True)
    if a < b:
        result.append(1)
    else:
        result.append(miles[b - 1])

result.sort()
cnt = 0

for i in result:
    M -= i
    cnt += 1
    if M < 0:
        print(cnt - 1)
        break

if M > 0:
    print(cnt)

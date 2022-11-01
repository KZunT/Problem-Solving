N = int(input())
H = list(map(int, input().split()))

line = [0] * N

for person in range(1, N + 1):
    t = H[person - 1]
    cnt = 0
    for i in range(N):
        if cnt == t and line[i] == 0:
            line[i] = person
            break
        elif line[i] == 0:
            cnt += 1
print(*line)

N, M = map(int, input().split())
floor = []

for _ in range(N):
    floor.append(list(input()))

cnt = 0

for i in range(N):
    deco = ''
    for j in range(M):
        if floor[i][j] == '-':
            if floor[i][j] != deco:
                cnt += 1
        deco = floor[i][j]

for k in range(M):
    deco = ''
    for l in range(N):
        if floor[l][k] == '|':
            if floor[l][k] != deco:
                cnt += 1
        deco = floor[l][k]

print(cnt)

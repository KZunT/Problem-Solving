N = int(input())

coords = [[] for _ in range(N)]

for _ in range(N):
    X, Y = map(int, input().split())
    coords[Y - 1].append(X)

answer = 0

for coord in coords:

    coord.sort()
    if len(coord) <= 1:
        continue

    answer += abs(coord[0] - coord[1]) + abs(coord[-1] - coord[-2])

    for j in range(1, len(coord) - 1):
        answer += min(abs(coord[j] - coord[j - 1]), abs(coord[j] - coord[j + 1]))

print(answer)

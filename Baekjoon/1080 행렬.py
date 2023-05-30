N, M = map(int, input().split())
graphA = []
graphB = []
count = 0


def reverse_matrix(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            graphA[x][y] = 1 - graphA[x][y]


for _ in range(N):
    graphA.append(list(map(int, input())))

for _ in range(N):
    graphB.append(list(map(int, input())))

for i in range(N - 2):
    for j in range(M - 2):
        if graphA[i][j] != graphB[i][j]:
            reverse_matrix(i, j)
            count += 1
flag = 0

for i in range(N):
    for j in range(M):
        if graphA[i][j] != graphB[i][j]:
            flag = 1
            break

if flag == 1:
    print(-1)
else:
    print(count)

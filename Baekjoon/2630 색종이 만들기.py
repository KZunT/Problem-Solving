N = int(input())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

color_list = []


def divncon(start, end, n):
    color = paper[start][end]
    for i in range(start, start + n):
        for j in range(end, end + n):
            if paper[i][j] != color:
                n = n // 2
                divncon(start, end, n)
                divncon(start + n, end, n)
                divncon(start, end + n, n)
                divncon(start + n, end + n, n)
                return
    if color == 0:
        color_list.append(0)
    else:
        color_list.append(1)

divncon(0, 0, N)

print(color_list.count(0))
print(color_list.count(1))

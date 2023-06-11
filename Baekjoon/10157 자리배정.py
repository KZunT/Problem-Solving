C, R = map(int, input().split())

K = int(input())

if K > C * R:
    print(0)
    exit()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

seats = [[0] * C for _ in range(R)]
dt, x, y = 0, 0, 0

for i in range(1, C * R + 1):
    if i == K:
        print(y + 1, x + 1)
        break
    else:
        seats[x][y] = i
        x += dx[dt]
        y += dy[dt]

        if x < 0 or y < 0 or x >= R or y >= C or seats[x][y]:
            x -= dx[dt]
            y -= dy[dt]
            dt = (dt + 1) % 4
            x += dx[dt]
            y += dy[dt]

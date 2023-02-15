from collections import deque

def bfs(tomatoes):
    queue = deque()

    for t in tomatoes:
        queue.append(t)

    while queue:
        x, y = queue.popleft()  # x 세로 y 가로
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < N and -1 < ny < M:
                if box[nx][ny] == 0:
                    queue.append((nx, ny))
                    box[nx][ny] = box[x][y] + 1


M, N = map(int, input().split())  # M 가로 N 세로

box = []

for _ in range(N):
    box.append(list(map(int, input().split())))

ripe_tomato = []  # 익은 토마토
not_ripe_tomato = []  # 안익은 토마토

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe_tomato.append((i, j))
        if box[i][j] == 0:
            not_ripe_tomato.append((i, j))

if not_ripe_tomato == []:  # 이미 모두 익은 경우
    print(0)

else:
    bfs(ripe_tomato)

    maxi = 0
    for b in box:
        maxi = max(maxi, max(b))
        if 0 in b:
            maxi = 0
            break
    print(maxi - 1)

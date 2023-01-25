from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    land[x][y] = 0

    # 상하좌우 대각선 x가 위아래 y가 좌우
    dx_list = [1, -1, 0, 0, -1, -1, 1, 1]
    dy_list = [0, 0, -1, 1, -1, 1, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx_list[i]
            ny = y + dy_list[i]

            if 0 <= nx < h and 0 <= ny < w :
                if land[nx][ny] == 1:  # 범위 내에 있고 섬이라면
                    land[nx][ny] = 0
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    land = []

    cnt = 0

    for _ in range(h):
        land.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                cnt += 1
                bfs(i, j)
    print(cnt)
from collections import deque

T = int(input())


def knight_bfs(l, cur_x, cur_y, des_x, des_y, visited):
    queue = deque()
    queue.append((cur_x, cur_y))
    visited[cur_x][cur_y] = 1

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    while queue:
        x, y = queue.popleft()

        if x == des_x and y == des_y:
            print(visited[des_x][des_y] - 1)

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < l and -1 < ny < l:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

for _ in range(T):
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    des_x, des_y = map(int, input().split())

    visited = [[0 for _ in range(l)] for _ in range(l)]

    knight_bfs(l, cur_x, cur_y, des_x, des_y, visited)

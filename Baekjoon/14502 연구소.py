from collections import deque
from itertools import product
from itertools import combinations
import copy

def bfs(walls):
    queue = deque()
    box = copy.deepcopy(graph)

    for i, j in walls:  # 벽세우기
        if box[i][j] != 0:  # 벽을 3개 못세우는 경우
            return
        else:
            box[i][j] = 1

    for i in range(N):
        for j in range(M):
            if box[i][j] == 2:
                queue.append((i,j))

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
                    box[nx][ny] = 2

    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                cnt += 1

    result = max(result, cnt)


N, M = map(int, input().split()) # N 세로 , M 가로

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

coord = product(list(range(N)), list(range(M)))

wall = list(coord)

wall_list = list(combinations(wall,3))  # 벽 경우의 수 생성

result = 0

for walls in wall_list:
    bfs(walls)


print(result)

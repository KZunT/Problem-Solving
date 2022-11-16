from collections import deque

N, M = 10, 10

graph = []

for _ in range(N):
    s = input().replace('.', '1')
    s = s.replace('R', '0')
    s = s.replace('B', '3')
    s = s.replace('L', '4')
    graph.append(list(map(int, s)))

for row in range(N):  # row , col = 행,렬
    for col in range(M):
        if graph[row][col] == 3:
            B = (row, col)
        if graph[row][col] == 4:
            L = (row, col)

graph[L[0]][L[1]] = 1
graph[B[0]][B[1]] = 1


def bfs(x, y):
    # 상하좌우 이동을 명시
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))  # 기본 bfs 처럼 노드 1개가 아니라 x,y 의 좌표 튜플로 방문을 명시

    # graph[x][y] += cnt  # 현재 방문한 위치는 0으로 바꿔 다시 방문하지 않도록 함

    while queue:
        x, y = queue.popleft()  # 노드의 갱신

        for i in range(4):  # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어나는 경우 제한  - 정사각형이 아닌 직사각형이므로 N, M 으로 범위 제한
                continue

            if graph[nx][ny] == 0:  # 바위 인경우 이동 불가
                continue

            if graph[nx][ny] == 1:  # 만약 옆 노드가 연결되어 있다면
                graph[nx][ny] = graph[x][y] + 1  # 연결된 노드의 거리 값 증가
                queue.append((nx, ny))  # 큐에 삽입


bfs(L[0], L[1])

print(graph[B[0]][B[1]] - 2) # 인접할 경우 불 끄기 가능하므로 호수 인접 -1 농장 인접 -1
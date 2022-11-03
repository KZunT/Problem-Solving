from collections import deque

N, M = map(int, input().split(' '))

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


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

            if graph[nx][ny] == 0:  # 벽인경우 이동 불가
                continue

            if graph[nx][ny] == 1:  # 만약 옆 노드가 연결되어 있다면
                graph[nx][ny] = graph[x][y] + 1  # 연결된 노드의 거리 값 증가
                queue.append((nx, ny))  # 큐에 삽입

    return graph[N - 1][M - 1]


print(bfs(0, 0))  # 1,1 출발이지만 인덱스상 0,0

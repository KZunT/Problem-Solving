from collections import deque


def bfs(x, y):
    # 상하좌우 이동을 명시
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))  # 기본 bfs 처럼 노드 1개가 아니라 x,y 의 좌표 튜플로 방문을 명시

    graph[x][y] = 0  # 현재 방문한 위치는 0으로 바꿔 다시 방문하지 않도록 함

    while queue:
        x, y = queue.popleft()  # 노드의 갱신

        for i in range(4):  # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어나는 경우 제한 - 세로 N 가로 M
                continue

            if graph[nx][ny] == 1:  # 만약 옆 노드가 연결되어 있다면
                graph[nx][ny] = 0  # 연결된 노드는 방문처리
                queue.append((nx, ny))  # 큐에 삽입


T = int(input())  # 테스트 케이스

for _ in range(T):
    cnt = 0

    M, N, K = map(int, input().split(' '))

    # 그래프 만들기

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1 # 가로, 세로 범위 주의!

    for i in range(N):  # 모든 좌표 순회하면서 배추가 있는 지역에 bfs 실행
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)  # bfs 완료시 카운트 업
                cnt += 1

    print(cnt)

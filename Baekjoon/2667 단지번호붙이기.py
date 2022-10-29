from collections import deque

N = int(input())

# 그래프 만들기
graph = []

for _ in range(N):
    graph.append(list(map(int, list(input()))))


def bfs(graph, x, y):
    # 상하좌우 이동을 명시
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y)) # 기본 bfs 처럼 노드 1개가 아니라 x,y 의 좌표 튜플로 방문을 명시

    graph[x][y] = 0  # 현재 방문한 위치는 0으로 바꿔 다시 방문하지 않도록 함
    cnt = 1 # 단지 내 집의 개수, bfs 알고리즘 사용시 1단지 당 1개의 bfs 면 모든 탐색을 마친다.

    while queue:
        x, y = queue.popleft() # 노드의 갱신

        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위를 벗어나는 경우 제한
                continue

            if graph[nx][ny] == 1: # 만약 옆 노드가 연결되어 있다면
                graph[nx][ny] = 0 # 연결된 노드는 방문처리
                queue.append((nx, ny)) # 큐에 삽입
                cnt += 1 # 단지 내 집의 개수 증가
    return cnt


count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1] # 이중 반복문을 통해 모든 좌표중 1이 남아있는 곳에서 bfs 실행

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])
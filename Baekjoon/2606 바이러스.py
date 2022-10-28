from collections import deque

N = int(input())  # 컴퓨터 (노드) 수
E = int(input())  # 총 엣지 수

graph = [[0] * (N + 1) for _ in range(N + 1)]  # 인접 행렬 생성

for _ in range(E):
    v1, v2 = map(int, input().split(' '))
    graph[v1][v2] = graph[v2][v1] = 1  # 노드간 의 연결 0 인경우 연결 x, 1 인경우 연결

# BFS 로 풀어보자


v = 1  # 문제에서 1번컴퓨터부터 바이러스 시작이라고 명시함

queue = deque()  # 큐 생성
visited = [v]  # 방문 노드 리스트 생성
queue.append(v)  # 방문한 노드 큐에 삽입

while queue:  # 큐가 빌 때 까지 반복

    v = queue.popleft()  # 큐에서 꺼내기, 현재 노드의 갱신

    for n in range(1, N + 1):  # 모든 컴퓨터에 대해 반복
        if graph[v][n] == 1 and (n not in visited):  # 노드가 연결되어 있고 방문하지 않았다면
            visited.append(n)  # 방문 처리
            queue.append(n)  # 큐에 삽입

print(len(visited) - 1)  # 방문한 노드는 바이러스에 감염 1은 바이러스의 시작되는 컴퓨터이므로 1을 빼준다

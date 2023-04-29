from collections import deque

F, S, G, U, D = map(int, input().split())  # 순서대로 건물 높이, 내가 있는 층, 목적지 층, 올라가는 층 단위, 내려가는 층 단위


def bfs(current, destination):
    queue = deque()
    queue.append(current)
    visited[current] = 0

    while queue:
        x = queue.popleft()

        if x == destination:
            return visited[x]

        for nx in (x + U, x - D):  # 올라가거나 내려가는 경우의 수
            if 0 < nx <= F and visited[nx] == -1:  # 건물 내에서 방문을 안한 층 이라면
                queue.append(nx)
                visited[nx] = visited[x] + 1

    return "use the stairs"  # 탐색 이후에도 층이 맞지 않다면 return


visited = [-1] * (F + 1)  # 해당 층의 방문 여부 (0으로 초기화 시 문자열 return 시 문제가 생길 수 있다.)

print(bfs(S, G))

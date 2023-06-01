from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n + 1)]
    queue = deque([1])
    visited[1] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:  # 연결되어있는 노드 중 확인
            if visited[i] == 0:  # 방문을 안했다면 큐에 추가
                queue.append(i)
                visited[i] = visited[v] + 1  # 해당 노드의 거리를 현재 1과의 거리에서 +1 함

    print(visited)

    return visited.cnt(max(visited))
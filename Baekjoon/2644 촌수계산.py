from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)


N = int(input())
graph = [[] for _ in range(N + 1)]
p1, p2 = map(int, input().split())  # 촌수를 계산해야 되는 사람
M = int(input())

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N + 1)
bfs(p1)

print(visited[p2] if visited[p2] > 0 else -1)
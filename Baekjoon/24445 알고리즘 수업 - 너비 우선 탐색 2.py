from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs():
    cnt = 1
    queue = deque([R])
    visited[R] = 1

    while queue:
        u = queue.popleft()
        graph[u].sort(reverse=True)
        for v in graph[u]:
            if visited[v] == 0:
                cnt += 1
                visited[v] = cnt
                queue.append(v)

bfs()

for v in visited[1:]:
    print(v)

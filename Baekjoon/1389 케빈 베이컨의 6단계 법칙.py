import sys
from collections import deque


def bfs(graph, start):
    numbers = [0] * (N + 1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        n = queue.popleft()
        for idx in graph[n]:
            if idx not in visited:
                numbers[idx] = numbers[n] + 1
                visited.append(idx)
                queue.append(idx)
    return sum(numbers)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

result = []
for i in range(1, N + 1):
    result.append(bfs(graph, i))

print(result.index(min(result)) + 1)

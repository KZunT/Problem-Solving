from collections import deque
import sys
input=sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                answer[node] = x

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int,input().split())

    graph[x].append(y)
    graph[y].append(x)

bfs(1)

for i in range(2,N+1):
    print(answer[i])
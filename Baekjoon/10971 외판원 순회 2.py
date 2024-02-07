import sys

input = sys.stdin.readline
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
summation = 0
answer = sys.maxsize


def dfs(depth, x):
    global summation, answer
    if depth == N - 1:
        if costs[x][0]:
            summation += costs[x][0]
            if summation < answer:
                answer = summation
            summation -= costs[x][0]
        return
    for i in range(1, N):
        if visited[i] == 0 and costs[x][i]:
            visited[i] = 1
            summation += costs[x][i]
            dfs(depth + 1, i)
            visited[i] = 0
            summation -= costs[x][i]


dfs(0, 0)
print(answer)

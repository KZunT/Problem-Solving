from collections import deque

N = int(input())  # 동기의 수
M = int(input())  # 리스트의 길이

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

friends = [0] * (N + 1)
friends[1] = 1


def bfs():
    queue = deque()
    queue.append(1)

    while queue:
        x = queue.popleft()
        for num in graph[x]:
            if friends[num] == 0:
                friends[num] = friends[x] + 1
                queue.append(num)


bfs()
result = sum([1 for distance in friends if 2 <= distance <= 3])  # 친구의 친구까지만 합산 거리가 1이면 자기 자신이므로 제외, 0이면 연결되지 않았으므로 제외
print(result)

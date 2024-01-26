import heapq
import sys

input = sys.stdin.readline

max_num = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, cur = heapq.heappop(queue)

        if dist > distance[cur]:
            continue

        for n in graph[cur]:
            cost = dist + n[1]
            if cost < distance[n[0]]:
                distance[n[0]] = cost
                heapq.heappush(queue, (cost, n[0]))


N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]
distance = [max_num] * (D + 1)

for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    S, E, L = map(int, input().split())
    if E > D:  
        continue
    graph[S].append((E, L))

dijkstra(0)
print(distance[D])

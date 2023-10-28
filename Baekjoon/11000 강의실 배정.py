import heapq

N = int(input())

heap = []

for i in range(N):
    start, end = map(int, input().split())
    heap.append([start, end])

heap.sort()

room = []
heapq.heappush(room, heap[0][1])

for i in range(1, N):
    if heap[i][0] < room[0]:
        heapq.heappush(room, heap[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, heap[i][1])

print(len(room))

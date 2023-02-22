import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    order = int(input())
    if heap == [] and order == 0:
        print(0)
    else:
        if order == 0:
            print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (abs(order), order))

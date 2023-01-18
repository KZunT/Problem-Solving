import sys
import heapq
N = int(input())

heap = []

heapq.heapify(heap)

for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)
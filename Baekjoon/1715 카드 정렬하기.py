import heapq
import sys

input = sys.stdin.readline

N = int(input())
cards = []

for _ in range(N):
    num = int(input())
    heapq.heappush(cards, num)

result = 0

while len(cards) > 1:
    heap_1 = heapq.heappop(cards)
    heap_2 = heapq.heappop(cards)
    result += heap_1 + heap_2
    heapq.heappush(cards, heap_1 + heap_2)

print(result)

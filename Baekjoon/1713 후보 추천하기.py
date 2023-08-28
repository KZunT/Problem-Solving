import sys

input = sys.stdin.readline
import heapq

N = int(input().rstrip())
M = int(input().rstrip())

photo = {}
numbers = list(map(int, input().split()))

for num in numbers:
    if num not in photo:
        if len(photo) >= N:
            a = heapq.nsmallest(min(photo), photo, key=photo.get)
            photo.pop(a[0])
        photo[num] = 1
    else:
        photo[num] += 1

print(*sorted(photo.keys()))

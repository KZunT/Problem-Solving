from collections import deque
import sys

N = int(sys.stdin.readline())

queue = deque()

while True:
    num = int(sys.stdin.readline())
    if num == -1:
        break
    if num != 0 and len(queue) < N:
        queue.append(num)
    elif num == 0:
        queue.popleft()

if queue:
    print(*queue)
else:
    print("empty")

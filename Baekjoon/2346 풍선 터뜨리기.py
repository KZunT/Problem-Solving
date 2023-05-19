from collections import deque

N = int(input())
queue = deque(enumerate(map(int, input().split())))
result = []

while queue:
    idx, paper = queue.popleft()
    result.append(idx + 1)

    if paper > 0:
        queue.rotate(-(paper - 1))
    elif paper < 0:
        queue.rotate(-paper)

print(' '.join(map(str, result)))

from collections import deque

N, M = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])

index = list(map(int, input().split()))

cnt = 0

for num in index:
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        else:
            if queue.index(num) <= len(queue) // 2:
                queue.rotate(-1)
                cnt += 1
            else:
                queue.rotate(1)
                cnt += 1

print(cnt)

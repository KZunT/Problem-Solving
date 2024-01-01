from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
school = []
start = ()

for i in range(N):
    row = list(input().rstrip())
    for j in range(M):
        if row[j] == 'I':
            start = (i, j)
    school.append(row)

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * M for _ in range(N)]
answer = 0

queue = deque([start])
visited[start[0]][start[1]] = True

while (queue):
    x, y = queue.popleft()
    for dx, dy in dir:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:

            if school[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

                if school[nx][ny] == 'P':
                    answer += 1

print(answer if answer > 0 else 'TT')

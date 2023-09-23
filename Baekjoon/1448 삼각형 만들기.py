import sys
input = sys.stdin.readline

N = int(input())
straws = sorted([int(input()) for _ in range(N)], reverse=True)
answer = -1

for i in range(N - 2):
    if straws[i] < straws[i + 1] + straws[i + 2]:
        answer = straws[i] + straws[i + 1] + straws[i + 2]
        break

print(answer)

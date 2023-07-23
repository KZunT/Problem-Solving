import sys
input = sys.stdin.readline

N = int(input())

runners = {}

for _ in range(N):
    name = input()
    if name in runners:
        runners[name] += 1
    else:
        runners[name] = 1

for _ in range(N-1):
    name = input()
    if runners[name] == 1:
        del runners[name]
    elif name in runners:
        runners[name] -= 1

print(*runners)
import sys

input = sys.stdin.readline

tasks = []
answer = 0
N = int(input())

for _ in range(N):
    task = list(map(int, input().split()))
    if task[0] == 1:
        tasks.append((task[1], task[2]))

    if tasks:
        score, time = tasks.pop()
        time -= 1
        if time == 0:
            answer += score
        else:
            tasks.append((score, time))
print(answer)

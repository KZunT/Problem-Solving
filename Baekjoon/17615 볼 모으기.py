import sys
input = sys.stdin.readline

N = int(input())
M = list(map(str, input().strip()))

answer = []
red, blue = 0, 0

cnt = 0

for i in range(N):
    if M[i] == "R":
        red += 1

    if M[i] == "B" and red:
        cnt += red
        red = 0

answer.append(cnt)

cnt = 0
for i in range(N):
    if M[i] == "B":
        blue += 1

    if M[i] == "R" and blue:
        cnt += blue
        blue = 0

answer.append(cnt)

M.reverse()

cnt = 0
red = 0
for i in range(N):
    if M[i] == "R":
        red += 1

    if M[i] == "B" and red:
        cnt += red
        red = 0

answer.append(cnt)

blue = 0
cnt = 0
for i in range(N):
    if M[i] == "B":
        blue += 1

    if M[i] == "R" and blue:
        cnt += blue
        blue = 0

answer.append(cnt)

print(min(answer))
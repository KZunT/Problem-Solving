import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    word = input().rstrip()
    stack = []

    for i in range(len(word)):
        if stack:
            if word[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(word[i])
        else:
            stack.append(word[i])

    if not stack:
        cnt += 1

print(cnt)

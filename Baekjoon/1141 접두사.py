import sys

input = sys.stdin.readline

N = int(input())
words = [(input()).rstrip() for _ in range(N)]

words.sort(key=len)
answer = 0

for i in range(N):
    flag = False

    for j in range(i + 1, N):
        if words[i] == words[j][0:len(words[i])]:
            flag = True
            break
    if not flag:
        answer += 1

print(answer)

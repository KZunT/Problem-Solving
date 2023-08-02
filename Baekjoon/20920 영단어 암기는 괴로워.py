import sys

input = sys.stdin.readline

N, M = map(int, input().split())
word = {}
for _ in range(N):
    name = input().strip()

    if len(name) < M:
        continue

    if word.get(name):
        word[name][0] += 1
    else:
        word[name] = [1, len(name), name]

answer = sorted(word.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for ele in answer:
    print(ele[0])

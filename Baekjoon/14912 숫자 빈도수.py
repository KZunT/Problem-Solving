N, D = map(int, input().split())

answer = ""

for i in range(1, N + 1):
    answer += str(i)

print(answer.count(str(D)))

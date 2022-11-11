N, M = map(int, input().split())

DNA = []

for _ in range(N):
    DNA.append(input())

cnt = 0
result = ''

for i in range(M):
    count = [0, 0, 0, 0]  # A, C, G, T 개수
    for j in range(N):
        if DNA[j][i] == 'A':
            count[0] += 1
        elif DNA[j][i] == 'C':
            count[1] += 1
        elif DNA[j][i] == 'G':
            count[2] += 1
        elif DNA[j][i] == 'T':
            count[3] += 1

    idx = count.index(max(count))

    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'
    cnt += N - max(count)

print(result)
print(cnt)
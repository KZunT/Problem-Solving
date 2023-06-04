N, record, P = map(int, input().split())

if N == 0:
    print(1)
    exit()


scores = list(map(int, input().split()))
scores.append(record)
scores.sort(reverse=True)

rank = scores.index(record) + 1


if N == P and record == scores[-1]:
    print(-1)
else:
    print(rank)


import sys

N, P = map(int, sys.stdin.readline().split())
code = [[0] for x in range(7)]
cnt = 0

for i in range(N):
    n_line, n_fret = map(int, sys.stdin.readline().split())

    while code[n_line][-1] > n_fret:
        code[n_line].pop()
        cnt += 1
    if code[n_line][-1] == n_fret:
        continue

    code[n_line].append(n_fret)
    cnt += 1

print(cnt)
import sys
input = sys.stdin.readline

N = int(input())
room = [input().rstrip() for _ in range(N)]
row_cnt, col_cnt = 0, 0

for i in range(N):
    for j in room[i].split('X'):
        if len(j) >= 2:
            row_cnt += 1

for i in range(N):
    col = 0
    for j in range(N):
        if room[j][i] == '.':
            col += 1
        else:
            col = 0
        if col == 2:
            col_cnt += 1

print(row_cnt, col_cnt)

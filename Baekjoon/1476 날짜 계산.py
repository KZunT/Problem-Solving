E, S, M = map(int, input().split())

year = 1

cur_E, cur_S, cur_M = 1, 1, 1

while True:
    if E == cur_E and S == cur_S and M == cur_M:
        break

    cur_E += 1
    cur_S += 1
    cur_M += 1

    year += 1

    if cur_E > 15:
        cur_E = 1
    if cur_S > 28:
        cur_S = 1
    if cur_M > 19:
        cur_M = 1

print(year)

# (year - curE) % 15 == 0 처럼 계산도 가능
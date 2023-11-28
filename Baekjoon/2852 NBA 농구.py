N = int(input())

one_time = 0
two_time = 0

flag = 0

for i in range(N):
    team, time = input().split()
    M, S = map(int, time.split(':'))
    if team == '1':
        if flag == 0:
            one_time += 48 * 60 - (60 * M + S)
        flag += 1

        if flag == 0:
            if two_time > 0:
                two_time = two_time - (48 * 60 - (60 * M + S))
    else:
        if flag == 0:
            two_time += 48 * 60 - (60 * M + S)
        flag -= 1

        if flag == 0:
            if one_time > 0:
                one_time = one_time - (48 * 60 - (60 * M + S))

print('{:0>2}:{:0>2}'.format(one_time // 60, one_time % 60))
print('{:0>2}:{:0>2}'.format(two_time // 60, two_time % 60))

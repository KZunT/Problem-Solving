N = input()

origin = N

cnt = 0

while (True):

    if int(N) < 10:
        N = '0' + N

    N = str(int(str(int(N) % 10) + str((int(N) // 10 + int(N) % 10) % 10)))

    cnt += 1

    if N == origin:
        break

print(cnt)
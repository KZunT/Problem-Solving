N = int(input())
status = list(map(int, input().split()))
change = {1: 0, 0: 1}

for _ in range(int(input())):
    gender, num = map(int, input().split())
    i = 1
    if gender == 1:
        while num * i - 1 < N:
            status[num * i - 1] = change[status[num * i - 1]]
            i += 1
    elif gender == 2:
        status[num - 1] = change[status[num - 1]]
        while 1 <= num - i and num + i < N + 1 and status[num - i - 1] == status[num - 1 + i]:
            status[num - 1 - i] = change[status[num - 1 - i]]
            status[num - 1 + i] = change[status[num - 1 + i]]
            i += 1

for i in range(N):
    print(status[i], end=" ")
    if i % 20 == 19:
        print()

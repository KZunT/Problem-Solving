num = int(input())

cnt = 0

while num >= 0:

    if num % 5 == 0:
        cnt += int(num // 5)
        break

    num -= 3
    cnt += 1

if num < 0:
    print(-1)

else:
    print(cnt)
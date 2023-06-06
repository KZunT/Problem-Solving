N = input()
cnt = 0
while True:
    if len(N) < 2:
        break
    N = str(sum((map(int, list(N)))))
    cnt += 1

print(cnt)
print('YES' if int(N) % 3 == 0 else 'NO')

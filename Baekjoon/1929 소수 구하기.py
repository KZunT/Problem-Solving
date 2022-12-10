M, N = map(int, input().split())

for i in range(M, N + 1):
    if i == 1:  # 1은 소수가 아니므로 제외
        continue

    for j in range(2, int(i ** 0.5) + 1): # 절반만 검사
        if i % j == 0:  # 약수가 존재하므로 소수가 아님
            break
    else:
        print(i)

#에라토스테네스의 체 문제
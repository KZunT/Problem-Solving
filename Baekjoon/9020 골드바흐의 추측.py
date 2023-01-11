def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # 소수의 판별
        if num % i == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    x = num // 2  # 들어온 값을 절반으로 나눔 (중앙 부터 찾기)

    while True:
        if is_prime(x) and is_prime(num - x):  # 한 수가 소수이고 주어진 값 - 소수 = 소수 이면 출력
            print(num - x, x)  # 작은 수 부터 출력
            break
        else:  #
            x += 1

# pypy3 일 경우만 시간초과가 뜨지 않는다..

def brt(n):
    cnt = (2 * n) - (n + 1)
    for i in range(n + 1, 2 * n):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:  # 소수가 아닌 경우
                cnt -= 1
                break
    return cnt


while True:
    num = int(input())
    if num == 0:
        break
    elif num == 1:
        print(1)
    else:
        print(brt(num))

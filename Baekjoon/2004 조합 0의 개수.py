N, M = map(int, input().split())


def combination_num(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt


num_five = combination_num(N, 5) - combination_num(M, 5) - combination_num(N - M, 5)
num_two = combination_num(N, 2) - combination_num(M, 2) - combination_num(N - M, 2)

answer = min(num_five, num_two)
print(answer)

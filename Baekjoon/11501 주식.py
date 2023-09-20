T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    answer = stock[0]
    sum_stock = 0

    for i in range(1, N):
        if answer < stock[i]:
            answer = stock[i]
            continue
        sum_stock += answer - stock[i]

    print(sum_stock)

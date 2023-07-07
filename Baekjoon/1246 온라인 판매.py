N, M = map(int, input().split())
prices = [int(input()) for _ in range(M)]

egg = 0
std = 0
prices.sort()

for price in prices:
    if (M - prices.index(price)) > N:
        continue

    sell = price * (M - prices.index(price))

    if sell > egg:
        egg = sell
        std = price

print(std, egg)

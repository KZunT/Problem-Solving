import sys

input = sys.stdin.readline

N = int(input())

roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

total = roads[0] * prices[0]
min_price = prices[0]

for i in range(1, N - 1):
    if min_price > prices[i]:
        min_price = prices[i]

    total += min_price * roads[i]

print(total)

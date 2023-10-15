N = int(input())

A, B = map(int, input().split())
C = int(input())

answer = 0

pizzas = sorted([int(input()) for _ in range(N)], reverse=True)

for i in range(N + 1):
    price = A + B * i
    answer = max(answer, (C + sum(pizzas[:i])) // price)

print(answer)

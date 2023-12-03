N, W = map(int, input().split())

price = []

for _ in range(N):
    price.append(int(input()))

answer = 0

for i in range(N - 1):
    if price[i] < price[i+1]:
        if W // price[i] > 0:
            answer = W // price[i]
            W = W - (answer * price[i])
    elif price[i-1] < price[i] and answer > 0:
        W = W + answer * price[i]
        answer = 0

if answer > 0:
    W = W + answer * price[N - 1]

print(W)
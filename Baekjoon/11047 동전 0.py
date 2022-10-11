N, K = map(int,input().split(' '))

coin_list = []
cnt = 0

for i in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

for coin in coin_list:
    cnt += K // coin
    K = K % coin

print(cnt)
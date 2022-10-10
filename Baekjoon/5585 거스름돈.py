pay = 1000-int(input())

coin_list = [500, 100, 50, 10, 5, 1]

coin_cnt = 0

while(True):

    coin = [x for x in coin_list if x <= pay]
    pay = pay - max(coin)
    coin_cnt += 1

    if pay == 0:
        break

print(coin_cnt)
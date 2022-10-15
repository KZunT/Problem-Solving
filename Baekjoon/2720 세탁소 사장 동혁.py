case = int(input())


coin_list = [25, 10, 5, 1]

for i in range(case):

    pay = int(input())
    cnt_list = []

    for coin in coin_list:
        cnt_list.append(str(pay//coin))
        pay = pay % coin

    print(" ".join(cnt_list))

N = int(input())
prices = list(map(int, input().split()))

bnp, bnp_money = N, 0
timing, timing_money = N, 0
answer = []

for price in prices:

    bnp_money += bnp // price
    bnp = bnp % price

    answer.append(price)

    if len(answer) >= 4:
        if answer[0] > answer[1] > answer[2]:
            timing_money += timing // price
            timing = timing % price
        elif answer[0] < answer[1] < answer[2]:
            timing += timing_money * price  #
            timing_money = 0
        answer.pop(0)

if bnp + prices[-1] * bnp_money > timing + prices[-1] * timing_money:
    print('BNP')
elif bnp + prices[-1] * bnp_money < timing + prices[-1] * timing_money:
    print('TIMING')
else:
    print('SAMESAME')

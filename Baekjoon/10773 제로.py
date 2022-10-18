K = int(input())

money_list = []

for i in range(K):
    num = int(input())

    if num != 0: # 0이 아닐경우 추가
        money_list.append(num)
    else: # 0일경우 최근의 수를 지움
        money_list.pop(-1)

print(sum(money_list))


N = int(input())

hansu_list = []

for i in range(1, N + 1):
    num = str(i)
    if i < 100:
        hansu_list.append(num)
    elif int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]): # 1000 이하이기 때문에 가능
        hansu_list.append(num)

print(len(hansu_list))
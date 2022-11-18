N = int(input())

milk_list = []
cnt = 0

for _ in range(N):
    milk_list.append(int(input()))

milk_list.sort(reverse=True)

for i in range(len(milk_list)):
    if (i + 1) % 3 == 0:
        pass
    else:
        cnt += milk_list[i]

print(cnt)

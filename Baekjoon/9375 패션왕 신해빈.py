from collections import Counter

T = int(input())
for _ in range(T):
    wear_list = []
    N = int(input())

    for _ in range(N):
        wear = input().split()[1]
        wear_list.append(wear)
    wear_list = Counter(wear_list)

    cnt = 1
    for key in wear_list.keys():
        cnt *= wear_list[key] + 1

    print(cnt - 1)  # 경우의 수 출력

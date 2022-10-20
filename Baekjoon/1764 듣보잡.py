N, M = map(int, input().split(' '))

hear_list = []
see_list = []

for h in range(N):
    hear_list.append(input())

for s in range(M):
    see_list.append(input())

hear_see_list = list(set(hear_list) & set(see_list))
hear_see_list.sort()

print(len(hear_see_list))

for hear_see in hear_see_list:
    print(hear_see)
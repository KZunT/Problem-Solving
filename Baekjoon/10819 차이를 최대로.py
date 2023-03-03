from itertools import permutations

N = int(input())

array = list(map(int, input().split()))

numbers = list(permutations(array))

cnt_list = []

for num in numbers:
    cnt = 0
    for i in range(2, len(num) + 1):
        cnt += abs(num[i - 2] - num[i - 1])
    cnt_list.append(cnt)

print(max(cnt_list))

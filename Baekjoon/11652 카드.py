# 시간초과 난 코드

# N = int(input())
#
# num_list = []
#
# for _ in range(N):
#     num_list.append(int(input()))
#
# maxi = max(num_list, key=num_list.count)
#
# print(maxi)
import sys

N = int(input())

num_dict = {}

for _ in range(N):
    num = int(sys.stdin.readline())  # input() 사용하면 시간초과..
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

num = sorted(num_dict.items(), key=lambda x: (-x[1], x[0]))  # -x 는 내림차순 x는 오름차순의 이미

print(num[0][0])

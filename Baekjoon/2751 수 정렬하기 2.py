import sys

N = int(input())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline())) # input() 보다 시간이 빠르다.

num_list.sort()

for num in num_list:
    print(num)
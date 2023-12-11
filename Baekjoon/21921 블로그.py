import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

value = 0
value_list = [0]

for i in visitors:
    value += i
    value_list.append(value)

result = []

cnt = 0
while cnt + X <= N:
    result.append(value_list[cnt + X] - value_list[cnt])
    cnt += 1

if max(result) == 0:
    print('SAD')
else:
    print(max(result))
    print(result.count(max(result)))

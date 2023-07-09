N = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
total = sum(num_list)

answer = 0

for num in num_list:
    answer += num * (total - num)
    total -= num

print(answer)

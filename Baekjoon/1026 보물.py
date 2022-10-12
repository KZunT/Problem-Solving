n = int(input())
A_list = list(map(int, input().split(' ')))
B_list = list(map(int, input().split(' ')))

A_list.sort(reverse=True)
B_list.sort()

sum = 0

for a, b in zip(A_list, B_list):
    sum = sum + (a * b)

print(sum)
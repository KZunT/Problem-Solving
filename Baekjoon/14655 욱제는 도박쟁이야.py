N = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

first_sum, second_sum = 0, 0

for f, s in zip(first, second):
    first_sum += abs(f)
    second_sum += abs(f)

print(first_sum + second_sum)

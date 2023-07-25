N = int(input())

numbers = list(map(int, input().split()))

total = sum(numbers)

answer = 0

for num in numbers:
    total = total - num
    answer += num * total

print(answer)

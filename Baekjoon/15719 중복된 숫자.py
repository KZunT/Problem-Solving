N = int(input())
numbers = sum(map(int,input().split()))
result = 0

temp = ''
for num in numbers:
    if num == ' ':
        result += int(temp)
        temp = ''

    else:
        temp += num
result += int(temp)

answer = N * (N - 1) // 2
print(numbers - answer)

N = int(input())
M = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
start = 0
end = len(numbers) - 1
cnt = 0

while start < end:
    armor = numbers[start] + numbers[end]
    if armor < M:
        start += 1
    elif armor > M:
        end -= 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)

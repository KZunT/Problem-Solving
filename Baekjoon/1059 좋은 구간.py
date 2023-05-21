L = int(input())
numbers = list(map(int, input().split()))
n = int(input())

numbers.append(0)
numbers.sort()

cnt = 0

for i in range(len(numbers) - 1):
    if numbers[i] == n or numbers[i + 1] == n:  # 구간이 없을 경우
        break
    elif numbers[i] < n < numbers[i + 1]:
        cnt = (n - numbers[i]) * (numbers[i + 1] - n) - 1  # 구간이 있을 경우
        break

print(cnt)

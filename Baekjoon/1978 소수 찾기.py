N = int(input())

num_list = list(map(int, input().split()))

count = 0

for num in num_list:

    for i in range(2, num + 1):
        if num % i == 0:
            if num == i:
                count += 1  # 나누어 떨어진게 자기 자신일 경우만 +해줌
            break

print(count)

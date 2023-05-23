N = int(input())
number = [0 if i ** 0.5 % 1 else 1 for i in range(N + 1)]  # 제곱수는 1로 저장

min_val = 4

for i in range(int(N ** 0.5), 0, -1):
    if number[N]:  # n이 제곱수일 경우
        min_val = 1
        break
    elif number[N - i ** 2]:  # 나머지가 제곱수일 경우
        min_val = 2
        break
    else:
        for j in range(int((N - i ** 2) ** 0.5), 0, -1):
            if number[(N - i ** 2) - j ** 2]:  # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_val = 3

print(min_val)

# dp로 풀면 pypy만 시간 통과
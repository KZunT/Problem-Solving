N = int(input())

# 다이나믹 프로그래밍 (바텀업)

d = [0] * (N + 1)

for i in range(2, N + 1): # 연산이 필요한 단계는 2부터 이다.
    d[i] = d[i - 1] + 1  # 연산 횟수를 구하는 문제기 때문에 +1 을 해준다.
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[N])

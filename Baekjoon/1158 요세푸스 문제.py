N, K = map(int, input().split())

circle = list(range(1, N + 1))

idx = 0  #

result = []

for t in range(N):
    idx += K - 1
    if idx >= len(circle):  # 한바퀴 이상 돌 경우를 고려 인덱스를 나머지 값으로 변환
        idx = idx % len(circle)
    result.append(str(circle.pop(idx)))

print("<" + ", ".join(result) + ">")

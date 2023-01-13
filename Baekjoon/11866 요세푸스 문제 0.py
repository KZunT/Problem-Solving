N, K = map(int, input().split())

man_list = list(range(1, N + 1))

idx = 0  #

result = []

for t in range(N):
    idx += K - 1
    if idx >= len(man_list):  # 한바퀴 이상 돌 경우를 고려 인덱스를 나머지 값으로 변환
        idx = idx % len(man_list)
    result.append(str(man_list.pop(idx)))

print('<'+", ".join(result)+'>')
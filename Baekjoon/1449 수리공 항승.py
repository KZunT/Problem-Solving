N, L = map(int, input().split())
S = list(map(int, input().split()))

S.sort()

start = S[0]  # 물이 새는 시작점
end = S[0] + L  # 시작점에서 테이프로 막았을 때 도달하는 점
cnt = 1  # 물이 새는곳은 자연수 이므로 최소 1개 이상

for i in range(N):
    if start <= S[i] < end:  # 테이프가 다음 물 새는곳도 막았을 때 (테이프 추가 필요없음)
        continue
    else:  # 테이프 추가가 필요하고 길이 갱신
        start = S[i]
        end = S[i] + L
        cnt += 1

print(cnt)

N, K = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

country.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)  # 메달 순 정렬

idx = [country[i][0] for i in range(N)].index(K)  # K의 인덱스 찾기

for i in range(N):
    if country[idx][1:] == country[i][1:]:
        print(i + 1)
        break

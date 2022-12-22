N = int(input())

tri = [] # 삼각형 선언

for _ in range(N):
    tri.append(list(map(int, input().split())))

for i in range(1, N):  # i = 삼각형 층
    tri[i][0] = tri[i][0] + tri[i - 1][0]   # 삼각형 왼쪽 대각선, 오른쪽 대각선 선택 중 0 인덱스는 왼쪽 대각선 선택밖에 안되기때문에 이전 층의 0 인덱스의 값을 더함

    for j in range(1, len(tri[i]) - 1): # 가운데 인덱스들은 이전층 왼쪽 오른쪽 대각선중 큰 값을 더함
        tri[i][j] = tri[i][j] + max(tri[i - 1][j - 1], tri[i - 1][j])

    tri[i][len(tri[i])-1] = tri[i][len(tri[i])-1] + tri[i - 1][len(tri[i - 1])-1] # 삼각형 왼쪽 대각선, 오른쪽 대각선 선택 중 마지막 인덱스는 오른쪽 대각선 선택밖에 안되기때문에 이전 층의 마지막 인덱스의 값을 더함

print(max(tri[-1]))

N = int(input())
A = list(map(int, input().split()))

d = [0] * N

for i in range(N):  # 부분 수열의 끝
    for j in range(N):
        if A[i] > A[j] and d[i] < d[j]:  # 증가하는 수열이기 때문에, 수열을 탐색시에 현재 위치가 끝보다 작은 경우여야 함
            d[i] = d[j]  # 이전 dp 테이블 중 가장 큰 값 가져옴
    d[i] += 1  # 현재 자신의 수 보다 작으면서 이전의 수열 수 중 가장 큰 값에 +1 을 하면 부분수열을 얻을 수 있다.

print(max(d))

# 이해가 좀 힘들다.
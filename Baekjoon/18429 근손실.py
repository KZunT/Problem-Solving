def dfs(depth, weight):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        if check[i] or weight + kits[i] - K < 0:  # 무게가 500을 넘어가는지 체크
            continue

        check[i] = 1
        dfs(depth + 1, weight + kits[i] - K)
        check[i] = 0


N, K = map(int, input().split())
kits = list(map(int, input().split()))

check = [0] * N
cnt = 0

dfs(0, 0)

print(cnt)

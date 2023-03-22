def dfs(x):
    global answer

    if len(W_list) == 2:
        answer = max(answer, x)
        return

    for i in range(1, len(W_list) - 1):
        energy = W_list[i - 1] * W_list[i + 1] # i번째 구슬을 제거했을 때 나오는 에너지

        W = W_list.pop(i) # 에너지 구슬 제거
        dfs(x + energy) # 제거된 구슬로 에너지를 재귀적으로 탐색
        W_list.insert(i, W) # 제거한 에너지 구슬 추가


N = int(input())
W_list = list(map(int, input().split()))
answer = 0
dfs(0)
print(answer)
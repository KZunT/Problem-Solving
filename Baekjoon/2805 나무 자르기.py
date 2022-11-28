N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

start = 0
end = max(tree_list)

while start <= end:  # 최대값을 찾은경우 종료

    mid = (start + end) // 2

    cnt = 0

    for tree in tree_list: # 잘린 나무 계산
        if tree >= mid:
            cnt += tree - mid

    if cnt >= M:  # 잘린 나무가 넘치면 절단기를 높인다
        start = mid + 1
    else:  # 잘린 나무가 부족하면 절단기를 낮춘다
        end = mid - 1

print(end)
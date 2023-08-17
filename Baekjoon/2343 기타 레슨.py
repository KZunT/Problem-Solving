N, M = map(int, input().split())
lesson = list(map(int, input().split()))

answer = 0

left, right = max(lesson), sum(lesson)

while left <= right:
    mid = (left + right) // 2

    count, total = 0, 0

    for i in range(N):
        if total + lesson[i] > mid:
            count += 1
            total = 0
        total += lesson[i]

    if total:
        count += 1
    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)

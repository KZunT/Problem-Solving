# 투 포인터 문제
N, M = map(int, input().split())
number = list(map(int, input().split()))

left, right = 0, 1

cnt = 0

while left <= right <= N:

    selected = number[left:right]

    total = sum(selected)

    if total == M:
        cnt += 1
        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)

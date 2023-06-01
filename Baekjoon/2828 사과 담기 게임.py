N, M = map(int, input().split())
J = int(input())

start = 1
end = M
cnt = 0

for _ in range(J):
    position = int(input())

    if start <= position <= end:
        continue
    elif start > position:
        cnt += (start - position)
        end -= (start - position)
        start = position
    else:
        cnt += (position - end)
        start += (position - end)
        end = position

print(cnt)

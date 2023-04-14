N = int(input())
cities = list(map(int, input().split()))

money = int(input())

start, end = 0, max(cities)

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    pay = 0
    for i in cities:
        if i > mid:
            pay += mid
        else:
            pay += i
    if pay <= money:
        start = mid + 1
    else:
        end = mid - 1
print(end)

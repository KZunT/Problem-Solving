N = int(input())
day = list(map(int, input().split()))

day.sort(reverse=True)

for i in range(N):
    day[i] += i

print(max(day) + 1 + 1) # 묘목 자라는데 최대 걸리는 일 수 + 묘목 산 날 (1) + 이장님 다음날 방문 (1)
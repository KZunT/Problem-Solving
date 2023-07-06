N = int(input())
cows = sorted([[*map(int, input().split())] for _ in range(N)])

time = 0

for i in range(N):
    start, end = cows[i]
    if time < start:
        time = start
    time += end

print(time)

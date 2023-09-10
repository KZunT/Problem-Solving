T = int(input())

for _ in range(T):
    N = int(input())
    food = sum(list(map(int, input().split())))
    day = 1
    while True:
        if N < food:
            break
        day += 1
        food *= 4
    print(day)

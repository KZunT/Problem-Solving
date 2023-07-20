N, L = map(int, input().split())
cur = 0
time = 0

for _ in range(N):
    D, R, G = map(int, input().split())
    time += D - cur
    cur = D
    if time % (R + G) <= R:
        time += R - time % (R + G)
time += L - cur

print(time)

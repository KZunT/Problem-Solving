N = int(input())

x, y = 1, 0

for _ in range(N):
    x, y = (x + y) % 10, x % 10

print(x)

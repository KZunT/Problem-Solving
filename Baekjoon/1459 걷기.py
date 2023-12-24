X, Y, W, S = map(int, input().split())

t1 = (X + Y) * W

if (X + Y) % 2 == 0:
    t2 = max(X, Y) * S
else:
    t2 = (max(X, Y) - 1) * S + W

t3 = (min(X, Y) * S) + (abs(X - Y) * W)

print(min(t1, t2, t3))

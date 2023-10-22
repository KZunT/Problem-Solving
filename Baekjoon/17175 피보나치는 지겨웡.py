N = int(input())

if N < 2:
    print(1)
else:
    a, b = 1, 1
    for i in range(N - 1):
        a, b = a + b + 1, a
    print(a % 1000000007)

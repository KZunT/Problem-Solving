input()

n = 0

for i in [*sorted(map(int, input().split()))]:
    if n + 1 < i:
        break
    n += i

print(n + 1)

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = A - B

if len(result) == 0:
    print(0)

else:
    print(len(result))
    print(' '.join(map(str, sorted(result))))

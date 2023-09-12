N, M = map(int, input().split())
result = N * (N - 1) * (N - 2) // 6
combination = [set() for _ in range(N)]

for _ in range(M):
    num1, num2 = map(int, input().split())
    result -= (N - 2) - len(combination[num1 - 1] | combination[num2 - 1])
    combination[num1 - 1].add(num2)
    combination[num2 - 1].add(num1)

print(result)

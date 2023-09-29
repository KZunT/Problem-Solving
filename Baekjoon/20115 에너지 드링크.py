N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

answer = drinks[-1]

for i in range(N - 1):
    answer += drinks[i] / 2

print(answer)

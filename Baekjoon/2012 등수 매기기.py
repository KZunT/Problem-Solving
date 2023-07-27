import sys
input = sys.stdin.readline

N = int(input())

rank = sorted([int(input()) for _ in range(N)])

result = 0

for i in range(1, N + 1):
    result += abs(i - rank[i - 1])

print(result)

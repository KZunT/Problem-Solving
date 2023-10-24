import sys

input = sys.stdin.readline

N, K = map(int, input().split())

numbers = sorted(list(map(int, input().split())))

answer = 0

for i in range(1, K + 1):
    answer += numbers[-i] - i + 1

print(answer)

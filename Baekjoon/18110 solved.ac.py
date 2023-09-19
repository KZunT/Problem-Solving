import sys

input = sys.stdin.readline
N = int(input())

if N != 0:
    numbers = [int(input()) for _ in range(N)]
    numbers.sort()
    x = round(N * 0.15 + 0.0000001);
    sum_num = sum(numbers[x:N - x])
    result = round((sum_num / (N - 2 * x)) + 0.0000001)
    print(result)
else:
    print(0)

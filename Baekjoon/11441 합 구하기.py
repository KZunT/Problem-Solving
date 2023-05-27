import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
M = int(input())


num_sum = [0] * (N + 1)
for i in range(1, N + 1):  # 누적 합
    num_sum[i] = num_sum[i - 1] + number[i - 1]

for _ in range(M):
    start, end = map(int, input().split())
    print(num_sum[end] - num_sum[start - 1])
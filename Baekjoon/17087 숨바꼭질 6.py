import sys
import math

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] = abs(S - A[i])

answer = A[0]

for i in range(1, N):
    answer = math.gcd(answer, A[i])

print(answer)

import sys
import math

input = sys.stdin.readline

N, M, K = map(int, input().split())

dotN1 = (K - 1) // M + 1
dotM1 = K - (dotN1 - 1) * M
dotN2 = N - (dotN1 - 1)
dotM2 = M - (dotM1 - 1)

if K == 0:
    print((math.factorial(N + M - 2) // (math.factorial(N - 1) * math.factorial(M - 1))))
else:
    first = (math.factorial(dotN1 + dotM1 - 2) // (math.factorial(dotN1 - 1) * math.factorial(dotM1 - 1)))
    second = (math.factorial(dotN2 + dotM2 - 2) // (math.factorial(dotN2 - 1) * math.factorial(dotM2 - 1)))
    print(first * second)

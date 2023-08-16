import sys

input = sys.stdin.readline


def gcd_r(a, b):
    if b == 0:
        return a
    else:
        return gcd_r(b, a % b)


A, B = map(int, input().split())

print('1' * gcd_r(A, B))

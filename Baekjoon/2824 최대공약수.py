import sys
import math
input = sys.stdin.readline


def multiply(lst):
    return eval('*'.join([str(n) for n in lst]))


N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

A = multiply(N_lst)
B = multiply(M_lst)

print('%s' % str(math.gcd(A, B))[-9:])

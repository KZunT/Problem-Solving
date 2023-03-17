import sys

input = sys.stdin.readline

N, M = map(int, input().split())
code = {}

for _ in range(N):
    site, pw = input().split()
    code[site] = pw

for _ in range(M):
    print(code[input().rstrip()])

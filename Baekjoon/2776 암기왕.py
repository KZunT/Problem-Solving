import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    note1 = set(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        print(1 if num in note1 else 0)

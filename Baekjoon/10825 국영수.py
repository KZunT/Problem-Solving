import sys
N = int(input())
input = sys.stdin.readline

report = []

for _ in range(N):
    report.append(input().split())

report.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for r in report:
    print(r[0])

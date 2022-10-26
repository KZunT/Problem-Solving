import sys

N = int(sys.stdin.readline())
coord = []

for i in range(N):
    coord.append(list(map(int, sys.stdin.readline().split())))

coord.sort(key=lambda x: (x[0], x[1]))

for co in coord:
    print(co[0], co[1])
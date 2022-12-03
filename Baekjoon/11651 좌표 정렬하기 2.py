import sys

N = int(sys.stdin.readline())

coord_list = []

for i in range(N):
    coord_list.append(list(map(int, sys.stdin.readline().split())))

coord_list.sort(key=lambda x: (x[1], x[0]))

for i in coord_list:
    print(i[0], i[1])

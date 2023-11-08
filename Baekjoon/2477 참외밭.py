import sys

input = sys.stdin.readline
K = int(input())

height = []
width = []
total = []

for i in range(6):
    dir, length = map(int, input().split())
    if dir == 1 or dir == 2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)

bigbox = max(height) * max(width)

maxh_idx = total.index(max(height))

max_widx = total.index(max(width))

small_list1 = abs(total[maxh_idx - 1] - total[(maxh_idx - 5 if maxh_idx == 5 else maxh_idx + 1)])
small_list2 = abs(total[max_widx - 1] - total[(max_widx - 5 if max_widx == 5 else max_widx + 1)])

area = bigbox - (small_list1 * small_list2)

print(area * K)

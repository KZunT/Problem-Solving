W, H = map(int, input().split())
N = int(input())
width = [0, W]
height = [0, H]

for _ in range(N):
    line, num = map(int, input().split())
    if line:
        width.append(num)
    else:
        height.append(num)

width.sort()
height.sort()

max_area = 0

for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i + 1] - width[i]
        y = height[j + 1] - height[j]
        max_area = max(max_area, x * y)

print(max_area)

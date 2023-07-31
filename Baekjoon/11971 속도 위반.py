import sys
input = sys.stdin.readline

N, M = map(int, input().split())

first = []
second = []

for _ in range(N):
    road, speed = map(int, input().split())
    for _ in range(road):
        first.append(speed)

for _ in range(M):
    road, speed = map(int, input().split())
    for _ in range(road):
        second.append(speed)

temp = 0

for i in range(100):
    if second[i] - first[i] > temp:
        temp = second[i] - first[i]

print(temp)
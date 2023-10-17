import sys

input = sys.stdin.readline


N = int(input())
string = input()

colors = {'B': 0, 'R': 0}
colors[string[0]] += 1

for i in range(1, N):
    if string[i] != string[i - 1]:
        colors[string[i]] += 1

result = min(colors['B'], colors['R']) + 1

print(result)

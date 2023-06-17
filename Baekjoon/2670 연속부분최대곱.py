N = int(input())

floats = []

for _ in range(N):
    floats.append(float(input()))

for i in range(1, N):
    floats[i] = max(floats[i], floats[i] * floats[i - 1])

print('%0.3f' % max(floats))

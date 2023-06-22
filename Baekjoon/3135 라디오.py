A, B = map(int, input().split())
N = int(input())

record = []

for i in range(N):
    record.append(abs(int(input()) - B))

print(min(abs(A - B), min(record) + 1))

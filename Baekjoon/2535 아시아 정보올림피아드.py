N = int(input())

students = []

for _ in range(N):
    students.append(list(map(int, input().split())))

students.sort(key=lambda x: -x[2])

print(*students[0][:2])
print(*students[1][:2])

idx = 2

if students[0][0] == students[1][0]:
    while students[0][0] == students[idx][0]:
        idx += 1
print(*students[idx][:2])

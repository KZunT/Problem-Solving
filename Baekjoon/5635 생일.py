N = int(input())

stu_list = []

for _ in range(N):
    name, day, month, year = input().split()
    stu_list.append((name, int(day), int(month), int(year)))

stu_list.sort(key=lambda x: (x[3], x[2], x[1]))

print(stu_list[-1][0])
print(stu_list[0][0])

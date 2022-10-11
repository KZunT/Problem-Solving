n = int(input())
time_list = list(map(int, input().split(' ')))

time_list.sort()

whole_time = 0
private_time = 0

for time in time_list:
    private_time += time
    whole_time += private_time

print(whole_time)
import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))


def get_clock_num(n):
    min_val = int(''.join(map(str, n)))
    for i in range(1, 4):
        temp = int(''.join(map(str, n[i:] + n[:i])))
        if min_val > temp:
            min_val = temp
    return min_val


clock_number = get_clock_num(numbers)

cnt = 1

for i in range(1111, clock_number):
    if '0' not in list(str(i)) and i == get_clock_num(list(map(int, str(i)))):
        cnt += 1
print(cnt)

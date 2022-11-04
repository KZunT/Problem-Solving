N = int(input())

serial_list = []


def sum_num(word):
    sum = 0
    for s in word:
        if s.isdecimal() == True:
            sum += int(s)
    return sum


for _ in range(N):
    serial_list.append(input())

serial_list.sort(key=lambda x: (len(x), sum_num(x), x)) # sort 안의 lambda 식을 통해 정렬기준 1,2,3 ... 순으로 순위를 둘 수 있다.

for serial in serial_list:
    print(serial)

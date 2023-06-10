# s = 1 일경우에 예외 발생
#
# s = int(input())
#
# sum = 0
#
# for n in range(1, s+1):
#     sum += n
#
#     if sum > s:
#         break
#
# print(n-1)
#

s = int(input())

total = 0
count = 0

while(True):

    count += 1
    total += count

    if total > s:
        break

print(count-1)
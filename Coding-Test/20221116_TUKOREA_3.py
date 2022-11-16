import re

M1, M2, N = map(int, input().split(' '))

first_c = input()
second_c = input()
mse = input()

first_code = mse
second_code = mse

for f, in first_c:
    first_code = re.sub(f + '{1,3}', f, first_code)

for s in second_c:
    second_code = re.sub(s + '{1,3}', s, second_code)

if first_c in first_code:
    print('YES')
else:
    print('NO')

if second_c in second_code:
    print('YES')
else:
    print('NO')

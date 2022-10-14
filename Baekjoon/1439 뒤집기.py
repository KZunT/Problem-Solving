import re

s = input()

# 0과 1을 정규표현식으로 찾아내어 비교

zero = re.compile('[' + '0' + ']+')

zero_cnt = zero.findall(s)

one = re.compile('[' + '1' + ']+')

one_cnt = one.findall(s)

if len(zero_cnt) < len(one_cnt):
    print(len(zero_cnt))

else:
    print(len(one_cnt))


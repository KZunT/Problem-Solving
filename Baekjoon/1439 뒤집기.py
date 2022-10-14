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


# 문자열을 순회하면서 0 과 1이 변할때마다 count 를 더하고 최종적으로 2로 나눠 출력하는 코드 추가

# S = input()
# count = 0
# for i in range(len(S)-1):
#     if S[i] != S[i+1]:
#         count += 1
# print((count + 1) // 2)
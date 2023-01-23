# def solution(s):
#     answer = []
#     dup_list = []
#     for i in range(1,len(s)): # 압축 크기
#         num = []    # 중복되는 수
#         cur = s[:i]
#         j = i   # 현재 인덱스
#         cnt = 1

#         while True:

#             if j > len(s):
#                 break

#             if cur == s[j:j+i]:
#                 cnt += 1
#             else :
#                 cur = s[j:j+i]
#                 if cnt != 0 and cnt != 1:
#                     num.append(cnt)
#                 cnt = 1
#             j += i

#         if num != []:
#             dup_list.append((i,num))

#     if dup_list == []:
#         return len(s)

#     for dup in dup_list:
#         dup_s = ''
#         dup_n = 0
#         for d in dup[1]:
#             dup_s += str(d)
#             dup_n += dup[0] * (d-1)
#         answer.append(len(s) +len(dup_s)-dup_n)

#     return min(answer)


def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        b = ''  # 새로운 문자열 생성
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s) + i, i):

            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:  # 중복이 있는경우
                    b = b + str(cnt) + tmp  # tmp는 끊어진 문자열
                else:
                    b = b + tmp  # 중복이 없다면 cnt 가 1이므로 표기안함

                tmp = s[j:j + i]
                cnt = 1
        result.append(len(b))

    return min(result)
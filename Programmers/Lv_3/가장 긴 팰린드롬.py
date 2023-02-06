# def solution(s):
#     answer = 0

#     # 홀수 길이인 경우

#     for i in range(len(s)): # i 는 기준점
#         max_len = min(i,len(s)-i-1)
#         for j in range(max_len+1):
#             if s[i-j : i+j+1] == s[i-j : i+j+1][::-1]:
#                 answer = max(answer, len(s[i-j : i+j+1]))

#     # 짝수 길이인 경우

#     for i in range(len(s)): # i 는 기준점
#         max_len = min(i,len(s)-i-1)
#         for j in range(max_len+1):
#             if s[i-j : i+j+2] == s[i-j : i+j+2][::-1]:
#                 answer = max(answer, len(s[i-j : i+j+2]))

#     return answer

def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            print(len(s), i, j)
            if s[j:j + i] == s[j:j + i][::-1]:
                return i
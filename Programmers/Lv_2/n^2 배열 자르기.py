def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]

## 시간초과 코드
# def solution(n, left, right):
#     answer = [[0] * n for _ in range(n)]

#     for i in range(1,n+1):
#         for j in range(i-1,i):
#             for k in range(i):
#                 answer[k][j] = i
#                 answer[j][k] = i

#     arr = []

#     li , l = left // n, left % n
#     ri , r = right // n, right % n

#     print(li , l )
#     print(ri , r )

#     arr.extend(answer[li][l:])

#     for i in range(li+1,ri):
#         arr.extend(answer[i])

#     arr.extend(answer[ri][:r+1])

#     return arr
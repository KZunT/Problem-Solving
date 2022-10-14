A, B = input().split(" ")

cnt = 1

while True:# B->A 가는 순서대로 문제의 역으로 계산

    if int(A) == int(B):
        break

    if B[-1] == '1':
        B = B[:len(B) - 1]

    elif int(B) % 2 == 0:
        B = str(int(B) // 2)

    else:   # 모든 조건이 용납되지 않으면 수를 만들 수 없음
        cnt = -1
        break

    if int(A) > int(B): # 1을 제거했을 때 0이 되어 2로 나누어 지지않을 수 있는 상황 처리
        cnt = -1
        break

    cnt += 1

if A == B: # 조건이 완성될 시
    print(cnt)
else:
    print(-1)


# 좀 더 깔끔한 코드 추가

# A,B = map(int, input().split())
#
# count = 1
#
# while True:
#   if A == B: # 조건 만족
#     break
#   elif (B % 2 != 0 and B % 10 != 1) or (A > B): # 예외 상황처리
#     count = -1
#     break
#   else:
#     if B % 10 == 1:
#       B //= 10
#       count += 1
#     else:
#       B //= 2
#       count += 1
#
# print(count)
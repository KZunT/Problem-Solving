N = int(input())

cnt = 0

num = 666

while True:
    if '666' in str(num):  # 666 이 나올때 마다 몇번째 666인지 카운트
        cnt += 1

    if cnt == N:
        print(num)
        break

    num += 1  # 666 없을경우 증가

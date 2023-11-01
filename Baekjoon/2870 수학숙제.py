import sys
input = sys.stdin.readline

N = int(input())

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

answer = []

for _ in range(N):
    M = list(map(str, input().strip("\n")))
    temp = []
    cnt = ""

    for i in M:
        if i in numbers:
            cnt += i
        else:
            if cnt:
                temp.append(int(cnt))
                cnt = ""
    if cnt:
        temp.append(int(cnt))

    answer += temp

answer.sort()

for num in answer:
    print(num)
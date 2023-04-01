import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    grade = [list(map(int, input().split())) for _ in range(N)]
    grade.sort()

    maxi = 0
    cnt = 1

    for i in range(1, len(grade)):
        if grade[i][1] < grade[maxi][1]:
            maxi = i
            cnt += 1

    print(cnt)
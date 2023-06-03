'''
문제 읽기 3:00

두 원 사이공간에 x,y가 정수인 경우? -> 원 위의 좌표도 포함

수학 문제인가..?

반지름은 정수로 주어진다.

흠.. 점이 원의 넓이 안에 있으면 되겠다. 3:15

엣지 케이스 해결을 해야한다. (두 점이 모두 정수일 때)

시간이 좀 오래걸린다. 어떻게 줄여야 할지는 모르겠다.

문제 풀이 3:35
'''

from math import sqrt

def solution(r1, r2):
    answer = 0
    for i in range(0, r1):
        answer += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
    for j in range(r1, r2):
        answer += int(sqrt(r2**2 - j**2))
    return answer * 4
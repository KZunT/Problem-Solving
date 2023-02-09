def cal(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (cal(a,b//2,c)**2)%c
    else:
        return ((cal(a,b//2,c)**2)*a)%c

A, B, C = map(int,input().split())
# divide and conquer 문제.
# B번 곱하는 것보다 B/2, B/2 X 2 가 더 효율 적 계산으로 적용됨.
# ex  2^32라면 2를 32번 곱하는 방법도 있지만, (2^16)^2로 해서 풀면 2를 16번 곱한 것을 다시 2번 곱하니 17번의 연산만으로 끝낼 수 있어 시간이 훨씬 적게 든다. 이를 계속 해보면 {(2^8)^2}^2 이렇게 풀면 10번만에, [{(2^4)^2}^2]^2 이렇게 풀면 7번만에 끝낼 수 있어 시간이 획기적으로 주는 것이다.

print(cal(A,B,C))
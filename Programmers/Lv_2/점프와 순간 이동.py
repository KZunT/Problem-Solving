def suit(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return suit(n // 2)
    else:
        return 1 + suit((n - 1) // 2)


def solution(n):
    return suit(n)

## 문제를 이해하면 쉬운코드 추가..
# def solution(n):
#     return bin(n).count('1')
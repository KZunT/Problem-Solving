N, M = map(int, input().split(':'))


def gcd(A, B):

    while B > 0:

        tmp = A
        A = B
        B = tmp % B

    return A

result = gcd(N, M)

print('%d:%d' % (N // result, M // result))

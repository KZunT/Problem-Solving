import string


def is_prime(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, int(num ** (0.5)) + 1):
        if num % i == 0:
            return False
    return True


# def convert_k(num, base):
#     number = string.digits + string.ascii_uppercase
#     q, r = divmod(num, base)
#     return convert_k(q, base) + number[r] if q else number[r]

def convert_k(n, k):
    s = ''
    while n:
        s += str(n % k)
        n = n // k
    return s[::-1]


def solution(n, k):
    answer = 0

    s = convert_k(n, k)
    num_list = s.split('0')

    for num in num_list:
        if num.isdigit() == True:
            if is_prime(int(num)) == True:
                answer += 1

    return answer
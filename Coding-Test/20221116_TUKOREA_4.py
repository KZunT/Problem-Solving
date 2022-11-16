b, N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


def change_10_to_n(n, value):
    n_list = []

    while n > 0:
        n, mod = divmod(n, value)
        n_list.append(mod)

    return n_list


def change_n_to_10(s, value):
    result = 0

    s = s[::-1]

    for i in range(len(s)):
        result += s[i] * (value ** i)

    return result


A_10 = change_n_to_10(A, b)
B_10 = change_n_to_10(B, b)

AB = A_10 * B_10

num_list = change_10_to_n(AB, b)

print(len(num_list))
print(' '.join(map(str, num_list[::-1])))

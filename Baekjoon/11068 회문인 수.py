def change_arith(x, y):
    res = []
    while x > 0:
        res.append(x % y)
        x = x // y

    return res[::-1]


T = int(input())

for _ in range(T):
    num = int(input())

    for i in range(2, 65):
        if change_arith(num, i) == change_arith(num, i)[::-1]:
            print(1)
            break
    else:
        print(0)

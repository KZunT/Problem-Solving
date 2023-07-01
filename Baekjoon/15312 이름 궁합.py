name = '32123323322122122212111221'
A = input()
B = input()

check = []

for i in range(len(A)):
    check.append(int(name[ord(A[i]) - 65]))
    check.append(int(name[ord(B[i]) - 65]))

for j in range(len(A) + len(B) - 1, 1, -1):
    calc = []
    for k in range(j):
        calc.append((check[k] + check[k + 1]) % 10)
    check = calc

print(str(check[0]) + str(check[1]))

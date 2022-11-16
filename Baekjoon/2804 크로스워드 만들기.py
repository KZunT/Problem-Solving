A, B = map(str, input().split())

for i in range(len(A)):
    if A[i] in B:
        col = i
        row = B.index(A[i])
        break

for j in range(len(B)):
    if j == row:
        print(A)
    else:
        print('.' * col + B[j] + '.' * (len(A) - col - 1))

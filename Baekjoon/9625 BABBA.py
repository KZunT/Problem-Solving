K = int(input())
A = [1]
B = [0]

for i in range(K):  # 반복할때마다 A와 B의 개수가 각각 규칙에 따라 늘어난다.
    A.append(B[i])
    B.append(B[i] + A[i])

print(A[-1], B[-1])

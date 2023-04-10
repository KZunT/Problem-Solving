import math

A, B = map(int, input().split())
C, D = map(int, input().split())

num = math.gcd(A * D + C * B, B * D)

print((A * D + C * B) // num, B * D // num)

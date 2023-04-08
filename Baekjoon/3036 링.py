import math

N = int(input())

rings = list(map(int, input().split()))

first_ring = rings[0]

for i in range(1, len(rings)):
    rotate = math.gcd(first_ring, rings[i]) # 최대 공약 수 이용
    A = first_ring // rotate
    B = rings[i] // rotate
    print('{}/{}'.format(A, B))

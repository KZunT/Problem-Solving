d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

# d[4] = d[3] + 1 , d[2] + 2, d[1] +3 으로 나타낼 수 있다.
for i in range(4, 11): # 점화식 생성 (규칙을 찾는것이 가장 중요)
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

T = int(input())

for _ in range(T):
    n = int(input())
    print(d[n])

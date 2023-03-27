N = int(input())
num_one = int(input())

num_other = []
cnt = 0
for _ in range(N - 1):
    num_other.append(int(input()))

num_other.sort(reverse=True)

if N == 1:
    print(0)
else:
    while num_other[0] >= num_one:
        num_one += 1
        num_other[0] -= 1
        cnt += 1
        num_other.sort(reverse=True)
    print(cnt)
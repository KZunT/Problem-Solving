N = int(input())

for _ in range(N):
    r, s = input().split()
    r = int(r)

    st = ''

    for i in s:
        st += i * r

    print(st)

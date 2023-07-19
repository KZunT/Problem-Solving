T = int(input())

for _ in range(T):
    N = int(input())
    init = list(input())
    target = list(input())
    cnt = []

    for i in range(N):
        if init[i] != target[i]:
            cnt.append(init[i])

    if not cnt:
        print(0)
    elif cnt.count("B") >= cnt.count("W"):
        print(cnt.count("B"))
    else:
        print(cnt.count("W"))
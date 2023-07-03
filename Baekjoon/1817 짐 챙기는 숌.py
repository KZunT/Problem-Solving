N, M = map(int, input().split())

cnt = 0

if N == 0:
    print(0)
else:
    boxes = list(map(int, input().split()))
    weight = 0
    cnt = 0
    for box in boxes:
        if box + weight <= M:
            weight += box
        else:
            weight = box
            cnt += 1

    print(cnt + 1)

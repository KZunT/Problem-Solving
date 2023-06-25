N = int(input())

arr = [float(input()) for i in range(7)]
arr.sort()

for _ in range(N - 7):
    cnt = float(input())
    if arr[6] > cnt:
        arr.pop()
        arr.append(cnt)
    arr.sort()

for num in arr:
    print("%.3f" % (num))

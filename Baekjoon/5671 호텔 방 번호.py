import sys

while True:
    data = sys.stdin.readline().rstrip()
    if not data:
        break
    cnt = 0
    N, M = map(int, data.split())

    for num in range(N, M + 1):
        if len(set(str(num))) == len(str(num)):
            cnt += 1
    print(cnt)

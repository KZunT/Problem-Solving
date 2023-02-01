N, S = map(int,input().split())
num = list(map(int,input().split()))

sub = []

cnt = 0

def sub_sum(start):
    global cnt

    if len(sub) > 0 and sum(sub) == S:
        cnt += 1

    for i in range(start,N):
        sub.append(num[i])
        sub_sum(i+1)
        sub.pop()

sub_sum(0)

print(cnt)
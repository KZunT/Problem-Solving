import sys

K, N = map(int, input().split())

lan_list = []

for _ in range(K):
    lan_list.append(int(sys.stdin.readline()))

start, end = 1, max(lan_list)

while start <= end:

    mid = (start + end) // 2
    res = 0

    for lan in lan_list:
        res += lan // mid

    if res >= N:  # 랜선이 더 많은 경우
        start = mid + 1  # 더 긴 길이로 잘라도 됨
    else:
        end = mid - 1

print(end)  # 최대 랜선 길이이므로 end 출력

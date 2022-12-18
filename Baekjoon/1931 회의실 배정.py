N = int(input())

meeting_list = []

for _ in range(N):
    meeting_start, meeting_end = map(int, input().split(' '))
    meeting_time = meeting_end - meeting_start
    meeting_list.append((meeting_start, meeting_end, meeting_time))

# 한번에 key 로 정렬하는것과 값이 다르다.
meeting_list.sort(key=lambda x: (x[0]))
meeting_list.sort(key=lambda x: (x[1]))

cnt = 0
end_time = 0

for m in meeting_list:
    if m[0] >= end_time:
        cnt += 1
        end_time = m[1]

print(cnt)
N = int(input())

member_list = []

for _ in range(N):
    member_list.append(input().split())

member_list.sort(key=lambda x: (int(x[0]))) # 나이순이므로 int 정렬..

for member in member_list:
    print(member[0], member[1])

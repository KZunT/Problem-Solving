N = int(input())

human_list = []
result = ''

for i in range(N):
    w, h = map(int, input().split(' '))
    human_list.append((w,h))

for i in human_list:

    rank = 1  # 1등 부터 시작 (초기값)

    for j in human_list:
        # 사람들 리스트를 순회하면서 등수 찾기
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    result = result+str(rank)+' '

print(result)
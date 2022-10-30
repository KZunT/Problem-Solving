N, L = map(int, input().split())

fruit_list = list(map(int, input().split()))  # 스네이크버드 앞에 놓인 과일들의 크기를 입력 받는다.
fruit_list.sort()  # 놓여 있는 과일들의 크기를 오름차순으로 정렬 한다.

for i in fruit_list:  # 놓여 있는 과일들을 하나 하나 불러 오는 구간이다.
    if i <= L:  # 만약 스네이크버드의 초기 길이 보다 과일의 크기가 작거나 같으면 진입한다.
        L += 1  # 스네이크버드의 초기 길이를 +1 시킨다.
    else:
        break

print(L)

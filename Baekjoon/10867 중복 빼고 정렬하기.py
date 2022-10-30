N = input()

num_list = list(set(map(int,input().split(' ')))) # 중복 제거하기

num_list.sort()

print(*num_list)
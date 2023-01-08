exp = input().split('-')  # - 기호를 기준으로 값을 더하여 가장 많은 값을 빼는것이 최소
sum_list = []

for e in exp:
    sum_list.append(sum(map(int, e.split('+'))))

if len(sum_list) == 0:
    print(sum_list[0])

else:
    print(sum_list[0] - sum(sum_list[1:]))

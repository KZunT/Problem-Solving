not_self_num_list = []

for num in range(1,10001):
    not_self_num = num
    for i in str(num):
        not_self_num += int(i)
    if not_self_num not in not_self_num_list:
        not_self_num_list.append(not_self_num)

for n in range(1,10001):
    if n not in not_self_num_list:
        print(n)

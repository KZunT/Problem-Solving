# 어디가 틀렸는지 잘 모르겠다.

# N = input()
# N = list(N.replace('9', '6'))
#
# max_num = max(N, key=N.count)
#
# if max_num == '6':
#     if N.count('6') % 2 == 0:
#         print(N.count(max_num) // 2)
#     else:
#         print(N.count(max_num) // 2 + 1)
# else:
#     print(N.count(max_num))

n = input()

a = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

for i in range(len(n)):
    if n[i] in ['6', '9']:
        a['6'] += 1
    else:
        a[n[i]] += 1

if a['6'] % 2 == 0:
    a['6'] = a['6'] // 2
else:
    a['6'] = a['6'] // 2 + 1

print(max(a.values()))

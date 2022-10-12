T = int(input())

btn_list = [300, 60, 10]

cnt_list = []

for btn in btn_list:
    cnt_list.append(str(T//btn))
    T = T % btn

if T == 0:
    print(' '.join(cnt_list))
else:
    print(-1)
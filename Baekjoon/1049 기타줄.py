N, M = map(int,(input().split(' ')))

single_list = []
package_list = []

money = 0

for i in range(M):
    p, s = map(int,(input().split(' ')))
    single_list.append(s)
    package_list.append(p)

single_list.sort()
package_list.sort()

if single_list[0] * 6 < package_list[0]: # 개별로 사는게 가장 싼 케이스
    money += N * single_list[0]

else: # 묶음으로 사는게 싼 케이스
    money += (N // 6) * package_list[0]
    N = N % 6

    if N != 0:
        if package_list[0] > single_list[0] * N: # 기타줄이 남았을 때 싱글로 남는것을 채우는게 싼 케이스
            money += single_list[0] * N
        else:                                    # 기타줄이 남았을 때 패키지로 채우는게 싼 케이스
            money += package_list[0]

print(money)
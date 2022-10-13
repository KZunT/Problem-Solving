n = input()
n = sorted(n, reverse=True)

sum = 0

if '0' not in n:	# 30의 배수가 되기 위해서 0이 마지막 자리에 와야하기때문에 0은 반드시 필요
    print(-1)

else:
    for i in n:
        sum += int(i)

    if sum % 3 != 0 :	# 3의 배수인 조건
        print(-1)
    else :              # 위의 조건이 충족 되었다면, n에 입력된 모든 숫자들로 30의 배수가 가능하기 때문에, 만들 수 있는 가장 큰 수가 30의 배수 중 가장 크다.
        print(''.join(n))
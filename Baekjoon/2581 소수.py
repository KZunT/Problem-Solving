M = int(input())
N = int(input())

prime_list = []

def isprime(num):
    if num == 1:  # 1은 소수가 아니므로 제외
        return False
    for i in range(2, int(num ** 0.5) + 1):  # 절반만 검사
        if num % i == 0:  # 약수가 존재하므로 소수가 아님
            return False
    return True

for i in range(M,N+1):
    if isprime(i):
        prime_list.append(i)

if prime_list == []:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
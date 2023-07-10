# *S로 선언한 이유 : Python에서 *을 붙여서 변수를 선언해주면 정해지지 않은 개수의 입력값이 들어온다는 의미이다.

N, *S = input().split()

while len(S) < int(N):
    data = input().split()
    S.extend(data)

answer = [int(num[::-1]) for num in S]
answer.sort()

for ele in answer:
    print(ele)
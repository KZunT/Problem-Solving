from math import gcd

def solution(arr):  # 최대공약수를 구하는 gcd() import
    answer = arr[0]

    for num in arr:  # 반복문을 처음부터 끝까지 돈다.
        answer = answer * num // gcd(answer, num)  # 두 수의 최소 공배수 구하기 (두 수의 곱 / 두수의 최대 공약수)

    return answer

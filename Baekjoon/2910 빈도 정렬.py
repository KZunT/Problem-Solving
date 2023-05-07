from collections import Counter

N, M = map(int, input().split())
message = list(map(int, input().split()))

code = Counter(message).most_common()  # most common 이용하여 빈도 수 대로 정렬된 값 가져오기

for num, cnt in code:  # 정렬된 수를 빈도에 맞춰 출력
    for _ in range(cnt):
        print(num, end=' ')

import sys

n = int(sys.stdin.readline())

word_list = []

for i in range(n):
    word_list.append(sys.stdin.readline().strip()) # strip 사용 안할경우 개행문자 \n\ 가 들어옴

word_list = list(set(word_list)) # 중복 제거..

word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)
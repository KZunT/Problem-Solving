import sys
word = list(sys.stdin.readline().rstrip())

index = 0
start = 0

while index < len(word):
    if word[index] == "<":       # 열린 괄호를 만나면
        index += 1
        while word[index] != ">":      # 닫힌 괄호를 만날 때 까지
            index += 1
        index += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[index].isalnum(): # 숫자나 알파벳을 만나면
        start = index
        while index < len(word) and word[index].isalnum():
            index+=1
        temp = word[start:index] # 숫자,알파벳 범위에 있는 것들을
        temp.reverse()       # 뒤집는다
        word[start:index] = temp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        index+=1                # 그냥 증가시킨다

print("".join(word))
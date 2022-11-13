cro_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c in cro_words:
    word = word.replace(c, '*')  # input 변수와 동일한 이름의 변수

print(len(word))

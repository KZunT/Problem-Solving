# 문제의 개수는 8개로 고정

score_list = []
ques_list = []
score_sum = 0

for ques in range(8):  # 점수 입력받기
    score_list.append((ques + 1, int(input())))

score_list.sort(key=lambda x: x[1], reverse=True)  # 점수 순 정렬

for score in score_list[:5]:  # 상위 5개 점수 정보 저장하기
    score_sum += score[1]
    ques_list.append(score[0])

ques_list.sort()

print(score_sum)
print(*ques_list)

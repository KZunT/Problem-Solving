N = int(input())

line = 0
end = 0
# 지그재그 형식상 짝수라인은 갈수록 분자가 1씩 늘고 분모가 1씩감소
# 홀수라인은 분자가 1씩감소 분모가 1씩 증가

while N > end:
    line += 1
    end += line

diff = end - N

if line % 2 == 0:  # 짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d" % (top, bottom))

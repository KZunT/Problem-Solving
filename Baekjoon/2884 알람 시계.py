H,M = map(int,input().strip().split(' '))

M -= 45

if M < 0:
    M += 60
    H -= 1

if H < 0:
    H +=24

print(H,M)

# 전부 초 단위 환산한 후 계산한 코드 작성

# a,b=map(int,input().split())
# x=a*60+b-45
# print(x//60%24,x%60)
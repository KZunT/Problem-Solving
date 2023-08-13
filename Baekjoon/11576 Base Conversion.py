A, B = map(int, input().split())
N = int(input())
number = list(map(int, input().split()))

word = 0
for i in range(N):
    word += number[N - i - 1] * A ** i

ans = ''

while word:
    ans = ' ' + ans
    ans = str(word % B) + ans
    word //= B

print(ans)
